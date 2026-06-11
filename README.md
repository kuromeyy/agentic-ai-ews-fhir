# agentic-ai-ews-fhir
Official repository for "Agentic AI Early Warning System with FHIR Interoperability". A context-aware patient monitoring and clinical anomaly detection framework built using n8n, MongoDB Atlas Vector Store (RAG), and Large Language Models.

# Agentic AI Early Warning System with FHIR Interoperability

Official source code and data assets for the research paper: **"Agentic AI Early Warning System with FHIR Interoperability"**.

This project implements an autonomous, context-aware **Early Warning System (EWS)** designed to overcome the limitations of rigid, traditional threshold-based patient monitoring. By integrating the **HL7 FHIR** standard, **Retrieval-Augmented Generation (RAG)**, and an event-driven automation framework, the system evaluates incoming physiological data against individual clinical histories and temporal trajectories.

---

## 🚀 Key Features

* **Standardized Interoperability:** Converts raw vital sign streams into HL7 FHIR-compliant JSON structures for semantic interoperability.
* **Context-Aware Anomaly Detection:** Leverages RAG to retrieve patient medical profiles and historical baselines, allowing the AI agent to distinguish chronic conditions from acute physiological deterioration.
* **Workflow Orchestration:** Powered by an event-driven architecture on the **n8n** automation platform.
* **Advanced Reasoning:** Driven by Large Language Models (LLMs) to perform multimodal clinical reasoning over complex, non-linear vital sign interactions.

---

## 📂 Repository Structure
```text
agentic-ai-ews-fhir/
│
├── data/
│   ├── historical_vital_signs/
│   │   └── historical_vital_signs.csv         # 24-hour lookback window master dataset (420 records)
│   │
│   ├── medical_records/
│   │   └── patient_medical_profiles.csv       # Personalized chronic baselines for 20 patients
│   │
│   ├── knowledge_base/
│   │   └── knowledgebase_rag.pdf              # Clinical reference guidelines & EWS standard thresholds
│   │
│   └── test_inputs/                           # Real-time simulation stream data partitioned per patient
│       ├── patient_1.csv                      # Simulated vital sign data for Patient 1
│       ├── patient_2.csv
│       └── ... (until patient_20.csv)
│
├── workflows/
│   └── agentic_fhir_ews_workflow.json        # Exported event-driven workflow blueprint for n8n
│
└── scripts/
    └── simulation_script.py                   # Python script to stream test inputs to the n8n webhook
