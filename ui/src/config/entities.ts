export type FieldType =
  | 'text'
  | 'textarea'
  | 'number'
  | 'decimal'
  | 'datetime'
  | 'boolean'
  | 'select'
  | 'tags'           // comma-separated list → string[]
  | 'remote-select'  // single select fetched from API → stores ID string
  | 'remote-multiselect'; // multi-select fetched from API → stores string[]

export interface FieldDef {
  name: string;
  label: string;
  type: FieldType;
  options?: string[];
  tableColumn?: boolean;
  // remote-select / remote-multiselect
  remoteSource?: string;    // API path, e.g. '/api/v1/intelligence-officers'
  remoteLabel?: string;     // field to show as option label, e.g. 'name'
  linkedNameField?: string; // also write the selected label into this sibling field
}

export interface EntityConfig {
  key: string;
  label: string;
  apiPath: string;
  category: string;
  nameField: string; // field used as display name in activity feed
  fields: FieldDef[];
}

// ─────────────────────────────────────────────────────────────────────────────
// Category order
// ─────────────────────────────────────────────────────────────────────────────
export const CATEGORY_ORDER = [
  'Intelligence',
  'HUMINT',
  'Cyber & OSINT',
  'SIGINT / MASINT',
  'GEO & IMINT',
  'Financial & Counter',
  'Medical & Tech',
  'Social & News',
  'People & Sources',
  'Investigations',
  'Operations',
  'Management',
];

// ─────────────────────────────────────────────────────────────────────────────
// Shared base-intel fields (all entities extending BaseIntel)
// ─────────────────────────────────────────────────────────────────────────────
const caseField: FieldDef = {
  name: 'case_id', label: 'Linked Case', type: 'remote-select',
  remoteSource: '/api/v1/intel-cases', remoteLabel: 'title',
};

const baseIntelFields: FieldDef[] = [
  caseField,
  { name: 'short_content', label: 'Short Content', type: 'textarea' },
];

// ─────────────────────────────────────────────────────────────────────────────
// Entity configs
// ─────────────────────────────────────────────────────────────────────────────
export const ENTITY_CONFIGS: EntityConfig[] = [
  // ── Intelligence ──────────────────────────────────────────────────────────
  {
    key: 'intel',
    label: 'Intel',
    apiPath: '/api/v1/intel',
    category: 'Intelligence',
    nameField: 'name',
    fields: [
      { name: 'name', label: 'Name', type: 'text', tableColumn: true },
      { name: 'short_description', label: 'Short Description', type: 'textarea', tableColumn: true },
      ...baseIntelFields,
    ],
  },
  {
    key: 'general-intel',
    label: 'General Intel',
    apiPath: '/api/v1/general-intel',
    category: 'Intelligence',
    nameField: 'title',
    fields: [
      caseField,
      { name: 'title', label: 'Title', type: 'text', tableColumn: true },
      { name: 'content', label: 'Content', type: 'textarea' },
      { name: 'classification', label: 'Classification', type: 'text', tableColumn: true },
      { name: 'source', label: 'Source', type: 'text', tableColumn: true },
      { name: 'date_collected', label: 'Date Collected', type: 'datetime' },
      { name: 'analyst', label: 'Analyst', type: 'text' },
      { name: 'tags', label: 'Tags', type: 'tags' },
      ...baseIntelFields,
    ],
  },
  {
    key: 'in-sum',
    label: 'Intelligence Summary',
    apiPath: '/api/v1/in-sum',
    category: 'Intelligence',
    nameField: 'title',
    fields: [
      caseField,
      { name: 'title', label: 'Title', type: 'text', tableColumn: true },
      { name: 'summary', label: 'Summary', type: 'textarea' },
      { name: 'period_from', label: 'Period From', type: 'datetime', tableColumn: true },
      { name: 'period_to', label: 'Period To', type: 'datetime', tableColumn: true },
      { name: 'prepared_by', label: 'Prepared By', type: 'text' },
      { name: 'classification', label: 'Classification', type: 'text' },
      ...baseIntelFields,
    ],
  },

  // ── HUMINT ────────────────────────────────────────────────────────────────
  {
    key: 'hum-int',
    label: 'HUMINT',
    apiPath: '/api/v1/hum-int',
    category: 'HUMINT',
    nameField: 'source_name',
    fields: [
      caseField,
      { name: 'source_name', label: 'Source Name', type: 'text', tableColumn: true },
      {
        name: 'hum_int_type',
        label: 'Type',
        type: 'select',
        options: ['INFORMANT', 'INTERROGATION', 'DEBRIEF', 'ELICITATION', 'SURVEILLANCE', 'LIAISON'],
        tableColumn: true,
      },
      { name: 'source_type', label: 'Source Type', type: 'text', tableColumn: true },
      { name: 'reliability_rating', label: 'Reliability Rating', type: 'number' },
      { name: 'contact_name', label: 'Contact Name', type: 'text' },
      { name: 'contact_email', label: 'Contact Email', type: 'text' },
      { name: 'time_location', label: 'Time / Location', type: 'text' },
      { name: 'context_background', label: 'Context / Background', type: 'textarea' },
      { name: 'source_information', label: 'Source Information', type: 'textarea' },
      ...baseIntelFields,
    ],
  },
  {
    key: 'informants',
    label: 'Informants',
    apiPath: '/api/v1/informants',
    category: 'HUMINT',
    nameField: 'code_name',
    fields: [
      caseField,
      { name: 'code_name', label: 'Code Name', type: 'text', tableColumn: true },
      { name: 'real_name', label: 'Real Name', type: 'text', tableColumn: true },
      { name: 'contact_info', label: 'Contact Info', type: 'text' },
      { name: 'reliability', label: 'Reliability', type: 'text', tableColumn: true },
      { name: 'notes', label: 'Notes', type: 'textarea' },
      ...baseIntelFields,
    ],
  },

  // ── Cyber & OSINT ─────────────────────────────────────────────────────────
  {
    key: 'cyb-int',
    label: 'Cyber Intel',
    apiPath: '/api/v1/cyb-int',
    category: 'Cyber & OSINT',
    nameField: 'incident_description',
    fields: [
      caseField,
      {
        name: 'incident_type',
        label: 'Incident Type',
        type: 'select',
        options: ['EMAIL_PHISHING', 'MALWARE', 'RANSOMWARE', 'DATA_BREACH', 'DDOS', 'INSIDER_THREAT', 'OTHER'],
        tableColumn: true,
      },
      { name: 'incident_description', label: 'Incident Description', type: 'textarea', tableColumn: true },
      { name: 'attribution', label: 'Attribution', type: 'text', tableColumn: true },
      { name: 'impact_assessment', label: 'Impact Assessment', type: 'textarea' },
      { name: 'malware_analysis', label: 'Malware Analysis', type: 'textarea' },
      { name: 'tt_ps', label: 'TTPs (comma-separated)', type: 'tags' },
      { name: 'indicators_of_compromise', label: 'IOCs (comma-separated)', type: 'tags' },
      { name: 'mitigation_recommendations', label: 'Mitigations', type: 'tags' },
      ...baseIntelFields,
    ],
  },
  {
    key: 'open-source-int',
    label: 'OSINT',
    apiPath: '/api/v1/open-source-int',
    category: 'Cyber & OSINT',
    nameField: 'source_name',
    fields: [
      caseField,
      { name: 'source_name', label: 'Source Name', type: 'text', tableColumn: true },
      { name: 'source_type', label: 'Source Type', type: 'text', tableColumn: true },
      { name: 'source_url', label: 'Source URL', type: 'text' },
      { name: 'target_name', label: 'Target Name', type: 'text', tableColumn: true },
      { name: 'target_location', label: 'Target Location', type: 'text' },
      { name: 'report_date', label: 'Report Date', type: 'datetime' },
      { name: 'analysis', label: 'Analysis', type: 'textarea' },
      { name: 'implications', label: 'Implications', type: 'textarea' },
      ...baseIntelFields,
    ],
  },

  // ── SIGINT / MASINT ───────────────────────────────────────────────────────
  {
    key: 'sig-int',
    label: 'SIGINT',
    apiPath: '/api/v1/sig-int',
    category: 'SIGINT / MASINT',
    nameField: 'signal_type',
    fields: [
      caseField,
      { name: 'signal_type', label: 'Signal Type', type: 'text', tableColumn: true },
      { name: 'signal_frequency', label: 'Frequency', type: 'text', tableColumn: true },
      { name: 'signal_source', label: 'Signal Source', type: 'text', tableColumn: true },
      { name: 'intercept_date_time', label: 'Intercept Date/Time', type: 'datetime' },
      { name: 'sender', label: 'Sender', type: 'text' },
      { name: 'receiver', label: 'Receiver', type: 'text' },
      { name: 'sender_location', label: 'Sender Location', type: 'text' },
      { name: 'receiver_location', label: 'Receiver Location', type: 'text' },
      { name: 'message_content', label: 'Message Content', type: 'textarea' },
      { name: 'analysis', label: 'Analysis', type: 'textarea' },
      { name: 'interpretation', label: 'Interpretation', type: 'textarea' },
    ],
  },
  {
    key: 'mas-int',
    label: 'MASINT',
    apiPath: '/api/v1/mas-int',
    category: 'SIGINT / MASINT',
    nameField: 'sensor_type',
    fields: [
      caseField,
      { name: 'sensor_type', label: 'Sensor Type', type: 'text', tableColumn: true },
      { name: 'measurement_type', label: 'Measurement Type', type: 'text', tableColumn: true },
      { name: 'location', label: 'Location', type: 'text', tableColumn: true },
      { name: 'date_time', label: 'Date/Time', type: 'datetime' },
      { name: 'data_summary', label: 'Data Summary', type: 'textarea' },
      { name: 'analysis', label: 'Analysis', type: 'textarea' },
      { name: 'findings', label: 'Findings', type: 'textarea' },
    ],
  },

  // ── GEO & IMINT ───────────────────────────────────────────────────────────
  {
    key: 'geo-int',
    label: 'GEOINT',
    apiPath: '/api/v1/geo-int',
    category: 'GEO & IMINT',
    nameField: 'location_name',
    fields: [
      caseField,
      { name: 'location_name', label: 'Location Name', type: 'text', tableColumn: true },
      { name: 'latitude', label: 'Latitude', type: 'decimal', tableColumn: true },
      { name: 'longitude', label: 'Longitude', type: 'decimal', tableColumn: true },
      { name: 'altitude', label: 'Altitude', type: 'decimal' },
      { name: 'collection_date', label: 'Collection Date', type: 'datetime' },
      { name: 'area_description', label: 'Area Description', type: 'textarea' },
      { name: 'analysis', label: 'Analysis', type: 'textarea' },
      { name: 'findings', label: 'Findings', type: 'textarea' },
    ],
  },
  {
    key: 'im-int',
    label: 'IMINT',
    apiPath: '/api/v1/im-int',
    category: 'GEO & IMINT',
    nameField: 'image_name',
    fields: [
      caseField,
      { name: 'image_name', label: 'Image Name', type: 'text', tableColumn: true },
      { name: 'image_source', label: 'Image Source', type: 'text', tableColumn: true },
      { name: 'capture_date', label: 'Capture Date', type: 'datetime', tableColumn: true },
      { name: 'image_format', label: 'Format', type: 'text' },
      { name: 'target_name', label: 'Target Name', type: 'text' },
      { name: 'target_location', label: 'Target Location', type: 'text' },
      { name: 'latitude', label: 'Latitude', type: 'decimal' },
      { name: 'longitude', label: 'Longitude', type: 'decimal' },
      { name: 'image_analysis', label: 'Image Analysis', type: 'textarea' },
      { name: 'interpretation', label: 'Interpretation', type: 'textarea' },
      { name: 'findings', label: 'Findings', type: 'textarea' },
      { name: 'key_features', label: 'Key Features (comma-separated)', type: 'tags' },
    ],
  },

  // ── Financial & Counter ───────────────────────────────────────────────────
  {
    key: 'financial-int',
    label: 'Financial Intel',
    apiPath: '/api/v1/financial-int',
    category: 'Financial & Counter',
    nameField: 'transaction_type',
    fields: [
      caseField,
      { name: 'transaction_type', label: 'Transaction Type', type: 'text', tableColumn: true },
      { name: 'amount', label: 'Amount', type: 'decimal', tableColumn: true },
      { name: 'transaction_date', label: 'Transaction Date', type: 'datetime', tableColumn: true },
      { name: 'counterparty', label: 'Counterparty', type: 'text', tableColumn: true },
      { name: 'investigating_agency', label: 'Investigating Agency', type: 'text' },
      { name: 'investigation_status', label: 'Investigation Status', type: 'text' },
      { name: 'regulatory_compliance_status', label: 'Compliance Status', type: 'text' },
      { name: 'suspicious_activity_description', label: 'Suspicious Activity', type: 'textarea' },
      { name: 'investigation_findings', label: 'Findings', type: 'textarea' },
      { name: 'involved_parties', label: 'Involved Parties (comma-separated)', type: 'tags' },
    ],
  },
  {
    key: 'counter-int',
    label: 'Counter Intel',
    apiPath: '/api/v1/counter-int',
    category: 'Financial & Counter',
    nameField: 'operation_name',
    fields: [
      caseField,
      { name: 'operation_name', label: 'Operation Name', type: 'text', tableColumn: true },
      { name: 'operation_start_date', label: 'Start Date', type: 'datetime', tableColumn: true },
      { name: 'operation_end_date', label: 'End Date', type: 'datetime' },
      { name: 'analysis', label: 'Analysis', type: 'textarea' },
      { name: 'findings', label: 'Findings', type: 'textarea' },
      { name: 'targets', label: 'Targets (comma-separated)', type: 'tags', tableColumn: true },
      { name: 'suspects', label: 'Suspects (comma-separated)', type: 'tags' },
      { name: 'tactics_used', label: 'Tactics (comma-separated)', type: 'tags' },
      { name: 'techniques_used', label: 'Techniques (comma-separated)', type: 'tags' },
      { name: 'countermeasures', label: 'Countermeasures (comma-separated)', type: 'tags' },
    ],
  },

  // ── Medical & Tech ────────────────────────────────────────────────────────
  {
    key: 'med-int',
    label: 'Medical Intel',
    apiPath: '/api/v1/med-int',
    category: 'Medical & Tech',
    nameField: 'patient_name',
    fields: [
      caseField,
      { name: 'patient_name', label: 'Patient Name', type: 'text', tableColumn: true },
      { name: 'age', label: 'Age', type: 'number', tableColumn: true },
      {
        name: 'gender',
        label: 'Gender',
        type: 'select',
        options: ['Male', 'Female', 'Other'],
        tableColumn: true,
      },
      { name: 'diagnosis', label: 'Diagnosis', type: 'text', tableColumn: true },
      { name: 'facility_name', label: 'Facility Name', type: 'text' },
      { name: 'facility_location', label: 'Facility Location', type: 'text' },
      { name: 'provider_name', label: 'Provider Name', type: 'text' },
      { name: 'provider_contact', label: 'Provider Contact', type: 'text' },
      { name: 'analysis', label: 'Analysis', type: 'textarea' },
      { name: 'findings', label: 'Findings', type: 'textarea' },
      { name: 'symptoms', label: 'Symptoms (comma-separated)', type: 'tags' },
      { name: 'treatments', label: 'Treatments (comma-separated)', type: 'tags' },
    ],
  },
  {
    key: 'tech-int',
    label: 'Tech Intel',
    apiPath: '/api/v1/tech-int',
    category: 'Medical & Tech',
    nameField: 'technology_name',
    fields: [
      caseField,
      { name: 'technology_name', label: 'Technology Name', type: 'text', tableColumn: true },
      { name: 'manufacturer', label: 'Manufacturer', type: 'text', tableColumn: true },
      { name: 'model', label: 'Model', type: 'text', tableColumn: true },
      { name: 'acquisition_source', label: 'Acquisition Source', type: 'text' },
      { name: 'acquisition_date', label: 'Acquisition Date', type: 'datetime' },
      { name: 'cost', label: 'Cost', type: 'decimal' },
      { name: 'technical_specifications', label: 'Technical Specifications', type: 'textarea' },
      { name: 'usage_history', label: 'Usage History', type: 'textarea' },
      { name: 'performance_analysis', label: 'Performance Analysis', type: 'textarea' },
      { name: 'integration_details', label: 'Integration Details', type: 'textarea' },
      { name: 'analysis', label: 'Analysis', type: 'textarea' },
      { name: 'findings', label: 'Findings', type: 'textarea' },
      { name: 'compatible_technologies', label: 'Compatible Technologies (comma-separated)', type: 'tags' },
    ],
  },

  // ── Social & News ─────────────────────────────────────────────────────────
  {
    key: 'news-articles',
    label: 'News Articles',
    apiPath: '/api/v1/news-articles',
    category: 'Social & News',
    nameField: 'title',
    fields: [
      caseField,
      { name: 'title', label: 'Title', type: 'text', tableColumn: true },
      { name: 'author', label: 'Author', type: 'text', tableColumn: true },
      { name: 'source', label: 'Source', type: 'text', tableColumn: true },
      { name: 'published_date', label: 'Published Date', type: 'datetime', tableColumn: true },
      { name: 'url', label: 'URL', type: 'text' },
      { name: 'content', label: 'Content', type: 'textarea' },
      ...baseIntelFields,
    ],
  },
  {
    key: 'social-media',
    label: 'Social Media',
    apiPath: '/api/v1/social-media',
    category: 'Social & News',
    nameField: 'username',
    fields: [
      caseField,
      { name: 'username', label: 'Username', type: 'text', tableColumn: true },
      { name: 'display_name', label: 'Display Name', type: 'text', tableColumn: true },
      { name: 'platform', label: 'Platform', type: 'text', tableColumn: true },
      { name: 'location', label: 'Location', type: 'text', tableColumn: true },
      { name: 'account_creation_date', label: 'Account Created', type: 'datetime' },
      { name: 'followers_count', label: 'Followers', type: 'number' },
      { name: 'following_count', label: 'Following', type: 'number' },
      { name: 'post_count', label: 'Posts', type: 'number' },
      { name: 'engagement_rate', label: 'Engagement Rate', type: 'text' },
      { name: 'sentiment_analysis', label: 'Sentiment Analysis', type: 'textarea' },
      { name: 'bio', label: 'Bio', type: 'textarea' },
      { name: 'private_account', label: 'Private Account', type: 'boolean' },
      { name: 'two_factor_authentication', label: '2FA Enabled', type: 'boolean' },
      ...baseIntelFields,
    ],
  },

  // ── People & Sources ──────────────────────────────────────────────────────
  {
    key: 'persons-of-interest',
    label: 'Persons of Interest',
    apiPath: '/api/v1/persons-of-interest',
    category: 'Investigations',
    nameField: 'full_name',
    fields: [
      caseField,
      { name: 'full_name', label: 'Full Name', type: 'text', tableColumn: true },
      { name: 'date_of_birth', label: 'Date of Birth', type: 'datetime', tableColumn: true },
      {
        name: 'gender',
        label: 'Gender',
        type: 'select',
        options: ['Male', 'Female', 'Other'],
        tableColumn: true,
      },
      { name: 'nationality', label: 'Nationality', type: 'text', tableColumn: true },
      { name: 'address', label: 'Address', type: 'text' },
      { name: 'phone', label: 'Phone', type: 'text' },
      { name: 'email', label: 'Email', type: 'text' },
      { name: 'occupation', label: 'Occupation', type: 'text' },
      { name: 'notes', label: 'Notes', type: 'textarea' },
      ...baseIntelFields,
    ],
  },
  {
    key: 'human-source',
    label: 'Human Sources',
    apiPath: '/api/v1/human-source',
    category: 'People & Sources',
    nameField: 'name',
    fields: [
      caseField,
      { name: 'name', label: 'Name', type: 'text', tableColumn: true },
      { name: 'source_type', label: 'Source Type', type: 'text', tableColumn: true },
      { name: 'reliability', label: 'Reliability', type: 'text', tableColumn: true },
      { name: 'contact_info', label: 'Contact Info', type: 'text' },
      { name: 'notes', label: 'Notes', type: 'textarea' },
    ],
  },
  {
    key: 'gov-source',
    label: 'Government Sources',
    apiPath: '/api/v1/gov-source',
    category: 'People & Sources',
    nameField: 'agency_name',
    fields: [
      caseField,
      { name: 'agency_name', label: 'Agency Name', type: 'text', tableColumn: true },
      { name: 'contact_name', label: 'Contact Name', type: 'text', tableColumn: true },
      { name: 'contact_email', label: 'Contact Email', type: 'text', tableColumn: true },
      { name: 'department', label: 'Department', type: 'text' },
      { name: 'notes', label: 'Notes', type: 'textarea' },
    ],
  },

  // ── Intel Case ────────────────────────────────────────────────────────────
  {
    key: 'intel-cases',
    label: 'Intel Cases',
    apiPath: '/api/v1/intel-cases',
    category: 'Investigations',
    nameField: 'title',
    fields: [
      caseField,
      { name: 'case_number', label: 'Case Number', type: 'text', tableColumn: true },
      { name: 'title', label: 'Title', type: 'text', tableColumn: true },
      {
        name: 'status', label: 'Status', type: 'select',
        options: ['Draft', 'Open', 'Active', 'Suspended', 'Closed', 'Archived'],
        tableColumn: true,
      },
      {
        name: 'priority', label: 'Priority', type: 'select',
        options: ['Low', 'Medium', 'High', 'Critical'],
        tableColumn: true,
      },
      {
        name: 'classification', label: 'Classification', type: 'select',
        options: ['UNCLASSIFIED', 'CONFIDENTIAL', 'SECRET', 'TOP SECRET', 'TS/SCI'],
        tableColumn: true,
      },
      { name: 'start_date', label: 'Start Date', type: 'datetime' },
      { name: 'end_date', label: 'End Date', type: 'datetime' },
      {
        name: 'case_officer_id', label: 'Case Officer', type: 'remote-select',
        remoteSource: '/api/v1/intelligence-officers', remoteLabel: 'name',
        linkedNameField: 'case_officer_name', tableColumn: true,
      },
      {
        name: 'ci_agent_id', label: 'CI Agent', type: 'remote-select',
        remoteSource: '/api/v1/ci-agents', remoteLabel: 'name',
        linkedNameField: 'ci_agent_name', tableColumn: true,
      },
      {
        name: 'assigned_analyst_ids', label: 'Assigned Analysts', type: 'remote-multiselect',
        remoteSource: '/api/v1/intelligence-analysts', remoteLabel: 'name',
      },
      {
        name: 'persons_of_interest_ids', label: 'Persons of Interest', type: 'remote-multiselect',
        remoteSource: '/api/v1/persons-of-interest', remoteLabel: 'name',
      },
      { name: 'area_of_interest', label: 'Area of Interest', type: 'text' },
      { name: 'description', label: 'Description', type: 'textarea' },
      { name: 'objective', label: 'Objective', type: 'textarea' },
      { name: 'conclusions', label: 'Conclusions', type: 'textarea' },
      { name: 'recommendations', label: 'Recommendations', type: 'textarea' },
      { name: 'lessons_learned', label: 'Lessons Learned', type: 'textarea' },
      { name: 'document_ids', label: 'Document IDs (comma-separated)', type: 'tags' },
      { name: 'tags', label: 'Tags (comma-separated)', type: 'tags' },
      { name: 'notes', label: 'Notes', type: 'textarea' },
    ],
  },

  // ── Intelligence Officers (S2/G2/J2) ─────────────────────────────────────
  {
    key: 'intelligence-officers',
    label: 'Intelligence Officers',
    apiPath: '/api/v1/intelligence-officers',
    category: 'Investigations',
    nameField: 'name',
    fields: [
      caseField,
      { name: 'name', label: 'Name', type: 'text', tableColumn: true },
      { name: 'rank', label: 'Rank', type: 'text', tableColumn: true },
      {
        name: 'designation', label: 'Designation', type: 'select',
        options: ['S2', 'G2', 'J2', 'N2', 'A2'],
        tableColumn: true,
      },
      { name: 'unit', label: 'Unit', type: 'text', tableColumn: true },
      { name: 'clearance_level', label: 'Clearance Level', type: 'select', options: ['UNCLASSIFIED', 'CONFIDENTIAL', 'SECRET', 'TOP SECRET', 'TS/SCI'] },
      { name: 'area_of_responsibility', label: 'Area of Responsibility', type: 'text' },
      { name: 'subordinate_analysts', label: 'Subordinate Analysts', type: 'number' },
      { name: 'reporting_to', label: 'Reporting To', type: 'text' },
      { name: 'current_assessment', label: 'Current Assessment', type: 'textarea' },
      { name: 'intelligence_priorities', label: 'PIRs (comma-separated)', type: 'tags' },
      { name: 'intelligence_products', label: 'Products (comma-separated)', type: 'tags' },
      { name: 'active', label: 'Active', type: 'boolean' },
      { name: 'contact_email', label: 'Contact Email', type: 'text' },
      { name: 'contact_phone', label: 'Contact Phone', type: 'text' },
      { name: 'notes', label: 'Notes', type: 'textarea' },
    ],
  },

  // ── Intelligence Analysts ────────────────────────────────────────────────
  {
    key: 'intelligence-analysts',
    label: 'Intelligence Analysts',
    apiPath: '/api/v1/intelligence-analysts',
    category: 'Investigations',
    nameField: 'name',
    fields: [
      caseField,
      { name: 'name', label: 'Name', type: 'text', tableColumn: true },
      { name: 'rank', label: 'Rank', type: 'text', tableColumn: true },
      { name: 'unit', label: 'Unit', type: 'text', tableColumn: true },
      { name: 'specialization', label: 'Specialization', type: 'text', tableColumn: true },
      { name: 'clearance_level', label: 'Clearance Level', type: 'select', options: ['UNCLASSIFIED', 'CONFIDENTIAL', 'SECRET', 'TOP SECRET', 'TS/SCI'] },
      { name: 'current_assignment', label: 'Current Assignment', type: 'text' },
      { name: 'reports_produced', label: 'Reports Produced', type: 'number' },
      { name: 'analytical_methods', label: 'Analytical Methods (comma-separated)', type: 'tags' },
      { name: 'systems_access', label: 'Systems Access (comma-separated)', type: 'tags' },
      { name: 'languages', label: 'Languages (comma-separated)', type: 'tags' },
      { name: 'active', label: 'Active', type: 'boolean' },
      { name: 'contact_email', label: 'Contact Email', type: 'text' },
      { name: 'contact_phone', label: 'Contact Phone', type: 'text' },
      { name: 'notes', label: 'Notes', type: 'textarea' },
    ],
  },

  // ── Intelligence Collectors ───────────────────────────────────────────────
  {
    key: 'intelligence-collectors',
    label: 'Intelligence Collectors',
    apiPath: '/api/v1/intelligence-collectors',
    category: 'Investigations',
    nameField: 'name',
    fields: [
      caseField,
      { name: 'name', label: 'Name', type: 'text', tableColumn: true },
      { name: 'rank', label: 'Rank', type: 'text', tableColumn: true },
      { name: 'unit', label: 'Unit', type: 'text', tableColumn: true },
      { name: 'collection_method', label: 'Collection Method', type: 'select', options: ['HUMINT', 'SIGINT', 'IMINT', 'OSINT', 'MASINT', 'OTHER'], tableColumn: true },
      { name: 'clearance_level', label: 'Clearance Level', type: 'select', options: ['UNCLASSIFIED', 'CONFIDENTIAL', 'SECRET', 'TOP SECRET', 'TS/SCI'] },
      { name: 'target_area', label: 'Target Area', type: 'text' },
      { name: 'active_operations', label: 'Active Operations', type: 'number' },
      { name: 'last_collection_date', label: 'Last Collection Date', type: 'datetime' },
      { name: 'collection_assets', label: 'Collection Assets (comma-separated)', type: 'tags' },
      { name: 'qualifications', label: 'Qualifications (comma-separated)', type: 'tags' },
      { name: 'languages', label: 'Languages (comma-separated)', type: 'tags' },
      { name: 'active', label: 'Active', type: 'boolean' },
      { name: 'contact_email', label: 'Contact Email', type: 'text' },
      { name: 'contact_phone', label: 'Contact Phone', type: 'text' },
      { name: 'notes', label: 'Notes', type: 'textarea' },
    ],
  },

  // ── CI Agents ────────────────────────────────────────────────────────────
  {
    key: 'ci-agents',
    label: 'CI Agents',
    apiPath: '/api/v1/ci-agents',
    category: 'Investigations',
    nameField: 'name',
    fields: [
      caseField,
      { name: 'name', label: 'Name', type: 'text', tableColumn: true },
      { name: 'rank', label: 'Rank', type: 'text', tableColumn: true },
      { name: 'unit', label: 'Unit', type: 'text', tableColumn: true },
      { name: 'ci_specialty', label: 'CI Specialty', type: 'select', options: ['Espionage Detection', 'Insider Threats', 'Sabotage', 'TSCM', 'FIE', 'Other'], tableColumn: true },
      { name: 'clearance_level', label: 'Clearance Level', type: 'select', options: ['UNCLASSIFIED', 'CONFIDENTIAL', 'SECRET', 'TOP SECRET', 'TS/SCI'] },
      { name: 'active_investigations', label: 'Active Investigations', type: 'number' },
      { name: 'cover_identity', label: 'Cover Identity', type: 'text' },
      { name: 'undercover', label: 'Undercover', type: 'boolean' },
      { name: 'target_threats', label: 'Target Threats (comma-separated)', type: 'tags' },
      { name: 'partner_agencies', label: 'Partner Agencies (comma-separated)', type: 'tags' },
      { name: 'active', label: 'Active', type: 'boolean' },
      { name: 'contact_email', label: 'Contact Email', type: 'text' },
      { name: 'contact_phone', label: 'Contact Phone', type: 'text' },
      { name: 'notes', label: 'Notes', type: 'textarea' },
    ],
  },

  // ── All-Source Analysts ───────────────────────────────────────────────────
  {
    key: 'all-source-analysts',
    label: 'All-Source Analysts',
    apiPath: '/api/v1/all-source-analysts',
    category: 'Investigations',
    nameField: 'name',
    fields: [
      caseField,
      { name: 'name', label: 'Name', type: 'text', tableColumn: true },
      { name: 'rank', label: 'Rank', type: 'text', tableColumn: true },
      { name: 'unit', label: 'Unit', type: 'text', tableColumn: true },
      { name: 'clearance_level', label: 'Clearance Level', type: 'select', options: ['UNCLASSIFIED', 'CONFIDENTIAL', 'SECRET', 'TOP SECRET', 'TS/SCI'], tableColumn: true },
      { name: 'fusion_methodology', label: 'Fusion Methodology', type: 'text' },
      { name: 'current_case_file_id', label: 'Current Case File ID', type: 'text' },
      { name: 'assessments_produced', label: 'Assessments Produced', type: 'number' },
      { name: 'sources_accessed', label: 'Sources Accessed (comma-separated)', type: 'tags' },
      { name: 'target_entities', label: 'Target Entities (comma-separated)', type: 'tags' },
      { name: 'tools_used', label: 'Tools Used (comma-separated)', type: 'tags' },
      { name: 'languages', label: 'Languages (comma-separated)', type: 'tags' },
      { name: 'active', label: 'Active', type: 'boolean' },
      { name: 'contact_email', label: 'Contact Email', type: 'text' },
      { name: 'contact_phone', label: 'Contact Phone', type: 'text' },
      { name: 'notes', label: 'Notes', type: 'textarea' },
    ],
  },

  // ── Operations ────────────────────────────────────────────────────────────
  {
    key: 'sit-rep',
    label: 'Situation Reports',
    apiPath: '/api/v1/sit-rep',
    category: 'Operations',
    nameField: 'title',
    fields: [
      caseField,
      { name: 'title', label: 'Title', type: 'text', tableColumn: true },
      { name: 'date_time', label: 'Date/Time', type: 'datetime', tableColumn: true },
      { name: 'location', label: 'Location', type: 'text', tableColumn: true },
      { name: 'situation', label: 'Situation', type: 'textarea' },
      { name: 'mission', label: 'Mission', type: 'textarea' },
      { name: 'execution', label: 'Execution', type: 'textarea' },
      { name: 'logistics', label: 'Logistics', type: 'textarea' },
      { name: 'command_signal', label: 'Command / Signal', type: 'textarea' },
      { name: 'prepared_by', label: 'Prepared By', type: 'text' },
    ],
  },
  {
    key: 'intel-documents',
    label: 'Intel Documents',
    apiPath: '/api/v1/intel-documents',
    category: 'Investigations',
    nameField: 'file_name',
    fields: [
      caseField,
      { name: 'file_name', label: 'File Name', type: 'text', tableColumn: true },
      {
        name: 'document_type',
        label: 'Document Type',
        type: 'select',
        options: ['NOTHING', 'REPORT', 'PHOTO', 'VIDEO', 'AUDIO', 'MAP', 'OTHER'],
        tableColumn: true,
      },
      { name: 'description', label: 'Description', type: 'textarea', tableColumn: true },
      { name: 'time_created', label: 'Time Created', type: 'datetime' },
      { name: 'long_description', label: 'Long Description', type: 'textarea' },
      { name: 'keywords', label: 'Keywords (comma-separated)', type: 'tags' },
      ...baseIntelFields,
    ],
  },
  {
    key: 'intel-investigation-files',
    label: 'Investigation Files',
    apiPath: '/api/v1/intel-investigation-files',
    category: 'Investigations',
    nameField: 'case_number',
    fields: [
      caseField,
      { name: 'case_number', label: 'Case Number', type: 'text', tableColumn: true },
      { name: 'started_date_time', label: 'Started', type: 'datetime', tableColumn: true },
      { name: 'ended_date_time', label: 'Ended', type: 'datetime' },
      {
        name: 'investigation_status',
        label: 'Status',
        type: 'select',
        options: ['INIT', 'ONGOING', 'SUSPENDED', 'CLOSED'],
        tableColumn: true,
      },
      { name: 'investigator_name', label: 'Investigator Name', type: 'text', tableColumn: true },
      { name: 'investigator_badge_number', label: 'Badge Number', type: 'text' },
      { name: 'description', label: 'Description', type: 'textarea' },
      { name: 'long_description', label: 'Long Description', type: 'textarea' },
      { name: 'investigator_note', label: 'Investigator Note', type: 'textarea' },
      { name: 'conclusion', label: 'Conclusion', type: 'textarea' },
      ...baseIntelFields,
    ],
  },

  // ── Management ────────────────────────────────────────────────────────────
  {
    key: 'operator-intel',
    label: 'Operator Intel',
    apiPath: '/api/v1/operator-intel',
    category: 'Management',
    nameField: 'operator_name',
    fields: [
      caseField,
      { name: 'operator_name', label: 'Operator Name', type: 'text', tableColumn: true },
      { name: 'operator_id', label: 'Operator ID', type: 'text', tableColumn: true },
      { name: 'role', label: 'Role', type: 'text', tableColumn: true },
      { name: 'clearance_level', label: 'Clearance Level', type: 'text' },
      { name: 'notes', label: 'Notes', type: 'textarea' },
    ],
  },
  {
    key: 'report-data',
    label: 'Report Data',
    apiPath: '/api/v1/report-data',
    category: 'Management',
    nameField: 'report_title',
    fields: [
      caseField,
      { name: 'report_title', label: 'Report Title', type: 'text', tableColumn: true },
      { name: 'report_type', label: 'Report Type', type: 'text', tableColumn: true },
      { name: 'created_date', label: 'Created Date', type: 'datetime', tableColumn: true },
      { name: 'author', label: 'Author', type: 'text', tableColumn: true },
      { name: 'content', label: 'Content', type: 'textarea' },
      { name: 'classification', label: 'Classification', type: 'text' },
    ],
  },
];

export function getEntityByKey(key: string): EntityConfig | undefined {
  return ENTITY_CONFIGS.find((e) => e.key === key);
}

export function groupedEntities(): Record<string, EntityConfig[]> {
  const result: Record<string, EntityConfig[]> = {};
  for (const cat of CATEGORY_ORDER) {
    const items = ENTITY_CONFIGS.filter((e) => e.category === cat);
    if (items.length > 0) result[cat] = items;
  }
  return result;
}
