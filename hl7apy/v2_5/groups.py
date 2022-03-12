from hl7apy.utils import iteritems

from .segments import SEGMENTS

GROUPS = {
    "ADR_A19_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, -1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
        ),
    ),
    "ADR_A19_PROCEDURE": (
        "sequence",
        (
            ["PR1", SEGMENTS["PR1"], (1, 1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
        ),
    ),
    "ADR_A19_QUERY_RESPONSE": (
        "sequence",
        (
            ["EVN", SEGMENTS["EVN"], (0, 1), "SEG"],
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
            ["NK1", SEGMENTS["NK1"], (0, -1), "SEG"],
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
            ["DB1", SEGMENTS["DB1"], (0, -1), "SEG"],
            ["OBX", SEGMENTS["OBX"], (0, -1), "SEG"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
            ["DG1", SEGMENTS["DG1"], (0, -1), "SEG"],
            ["DRG", SEGMENTS["DRG"], (0, 1), "SEG"],
            ["ADR_A19_PROCEDURE", None, (0, -1), "GRP"],
            ["GT1", SEGMENTS["GT1"], (0, -1), "SEG"],
            ["ADR_A19_INSURANCE", None, (0, -1), "GRP"],
            ["ACC", SEGMENTS["ACC"], (0, 1), "SEG"],
            ["UB1", SEGMENTS["UB1"], (0, 1), "SEG"],
            ["UB2", SEGMENTS["UB2"], (0, 1), "SEG"],
        ),
    ),
    "ADT_A01_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, -1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
        ),
    ),
    "ADT_A01_PROCEDURE": (
        "sequence",
        (
            ["PR1", SEGMENTS["PR1"], (1, 1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
        ),
    ),
    "ADT_A03_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, -1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
        ),
    ),
    "ADT_A03_PROCEDURE": (
        "sequence",
        (
            ["PR1", SEGMENTS["PR1"], (1, 1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
        ),
    ),
    "ADT_A05_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, -1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
        ),
    ),
    "ADT_A05_PROCEDURE": (
        "sequence",
        (
            ["PR1", SEGMENTS["PR1"], (1, 1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
        ),
    ),
    "ADT_A06_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, -1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
        ),
    ),
    "ADT_A06_PROCEDURE": (
        "sequence",
        (
            ["PR1", SEGMENTS["PR1"], (1, 1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
        ),
    ),
    "ADT_A16_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, -1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
        ),
    ),
    "ADT_A16_PROCEDURE": (
        "sequence",
        (
            ["PR1", SEGMENTS["PR1"], (1, 1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
        ),
    ),
    "ADT_A39_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["MRG", SEGMENTS["MRG"], (1, 1), "SEG"],
            ["PV1", SEGMENTS["PV1"], (0, 1), "SEG"],
        ),
    ),
    "ADT_A43_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["MRG", SEGMENTS["MRG"], (1, 1), "SEG"],
        ),
    ),
    "ADT_A45_MERGE_INFO": (
        "sequence",
        (
            ["MRG", SEGMENTS["MRG"], (1, 1), "SEG"],
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
        ),
    ),
    "BAR_P01_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, -1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
        ),
    ),
    "BAR_P01_PROCEDURE": (
        "sequence",
        (
            ["PR1", SEGMENTS["PR1"], (1, 1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
        ),
    ),
    "BAR_P01_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (0, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
            ["DB1", SEGMENTS["DB1"], (0, -1), "SEG"],
            ["OBX", SEGMENTS["OBX"], (0, -1), "SEG"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
            ["DG1", SEGMENTS["DG1"], (0, -1), "SEG"],
            ["DRG", SEGMENTS["DRG"], (0, 1), "SEG"],
            ["BAR_P01_PROCEDURE", None, (0, -1), "GRP"],
            ["GT1", SEGMENTS["GT1"], (0, -1), "SEG"],
            ["NK1", SEGMENTS["NK1"], (0, -1), "SEG"],
            ["BAR_P01_INSURANCE", None, (0, -1), "GRP"],
            ["ACC", SEGMENTS["ACC"], (0, 1), "SEG"],
            ["UB1", SEGMENTS["UB1"], (0, 1), "SEG"],
            ["UB2", SEGMENTS["UB2"], (0, 1), "SEG"],
        ),
    ),
    "BAR_P02_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["PV1", SEGMENTS["PV1"], (0, 1), "SEG"],
            ["DB1", SEGMENTS["DB1"], (0, -1), "SEG"],
        ),
    ),
    "BAR_P05_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, -1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
        ),
    ),
    "BAR_P05_PROCEDURE": (
        "sequence",
        (
            ["PR1", SEGMENTS["PR1"], (1, 1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
        ),
    ),
    "BAR_P05_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (0, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
            ["DB1", SEGMENTS["DB1"], (0, -1), "SEG"],
            ["OBX", SEGMENTS["OBX"], (0, -1), "SEG"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
            ["DG1", SEGMENTS["DG1"], (0, -1), "SEG"],
            ["DRG", SEGMENTS["DRG"], (0, 1), "SEG"],
            ["BAR_P05_PROCEDURE", None, (0, -1), "GRP"],
            ["GT1", SEGMENTS["GT1"], (0, -1), "SEG"],
            ["NK1", SEGMENTS["NK1"], (0, -1), "SEG"],
            ["BAR_P05_INSURANCE", None, (0, -1), "GRP"],
            ["ACC", SEGMENTS["ACC"], (0, 1), "SEG"],
            ["UB1", SEGMENTS["UB1"], (0, 1), "SEG"],
            ["UB2", SEGMENTS["UB2"], (0, 1), "SEG"],
            ["ABS", SEGMENTS["ABS"], (0, 1), "SEG"],
            ["BLC", SEGMENTS["BLC"], (0, -1), "SEG"],
            ["RMI", SEGMENTS["RMI"], (0, 1), "SEG"],
        ),
    ),
    "BAR_P06_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PV1", SEGMENTS["PV1"], (0, 1), "SEG"],
        ),
    ),
    "BAR_P10_PROCEDURE": (
        "sequence",
        (
            ["PR1", SEGMENTS["PR1"], (1, 1), "SEG"],
            ["GP2", SEGMENTS["GP2"], (0, 1), "SEG"],
        ),
    ),
    "BAR_P12_PROCEDURE": (
        "sequence",
        (
            ["PR1", SEGMENTS["PR1"], (1, 1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
        ),
    ),
    "BPS_O29_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["BPS_O29_TIMING", None, (0, -1), "GRP"],
            ["BPO", SEGMENTS["BPO"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["BPS_O29_PRODUCT", None, (0, -1), "GRP"],
        ),
    ),
    "BPS_O29_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["BPS_O29_PATIENT_VISIT", None, (0, 1), "GRP"],
        ),
    ),
    "BPS_O29_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "BPS_O29_PRODUCT": (
        "sequence",
        (
            ["BPX", SEGMENTS["BPX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "BPS_O29_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "BRP_O30_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["BRP_O30_TIMING", None, (0, -1), "GRP"],
            ["BPO", SEGMENTS["BPO"], (0, 1), "SEG"],
            ["BPX", SEGMENTS["BPX"], (0, -1), "SEG"],
        ),
    ),
    "BRP_O30_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["BRP_O30_ORDER", None, (0, -1), "GRP"],
        ),
    ),
    "BRP_O30_RESPONSE": ("sequence", (["BRP_O30_PATIENT", None, (0, 1), "GRP"],)),
    "BRP_O30_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "BRT_O32_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["BRT_O32_TIMING", None, (0, -1), "GRP"],
            ["BPO", SEGMENTS["BPO"], (0, 1), "SEG"],
            ["BTX", SEGMENTS["BTX"], (0, -1), "SEG"],
        ),
    ),
    "BRT_O32_RESPONSE": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (0, 1), "SEG"],
            ["BRT_O32_ORDER", None, (0, -1), "GRP"],
        ),
    ),
    "BRT_O32_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "BTS_O31_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["BTS_O31_TIMING", None, (0, -1), "GRP"],
            ["BPO", SEGMENTS["BPO"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["BTS_O31_PRODUCT_STATUS", None, (0, -1), "GRP"],
        ),
    ),
    "BTS_O31_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["BTS_O31_PATIENT_VISIT", None, (0, 1), "GRP"],
        ),
    ),
    "BTS_O31_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "BTS_O31_PRODUCT_STATUS": (
        "sequence",
        (
            ["BTX", SEGMENTS["BTX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "BTS_O31_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "CRM_C01_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PV1", SEGMENTS["PV1"], (0, 1), "SEG"],
            ["CSR", SEGMENTS["CSR"], (1, 1), "SEG"],
            ["CSP", SEGMENTS["CSP"], (0, -1), "SEG"],
        ),
    ),
    "CSU_C09_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["CSU_C09_VISIT", None, (0, 1), "GRP"],
            ["CSR", SEGMENTS["CSR"], (1, 1), "SEG"],
            ["CSU_C09_STUDY_PHASE", None, (1, -1), "GRP"],
        ),
    ),
    "CSU_C09_RX_ADMIN": (
        "sequence",
        (
            ["RXA", SEGMENTS["RXA"], (1, 1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, 1), "SEG"],
        ),
    ),
    "CSU_C09_STUDY_OBSERVATION": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (0, 1), "SEG"],
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["CSU_C09_TIMING_QTY", None, (0, -1), "GRP"],
            ["OBX", SEGMENTS["OBX"], (1, -1), "SEG"],
        ),
    ),
    "CSU_C09_STUDY_PHARM": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (0, 1), "SEG"],
            ["CSU_C09_RX_ADMIN", None, (1, -1), "GRP"],
        ),
    ),
    "CSU_C09_STUDY_PHASE": (
        "sequence",
        (
            ["CSP", SEGMENTS["CSP"], (0, 1), "SEG"],
            ["CSU_C09_STUDY_SCHEDULE", None, (1, -1), "GRP"],
        ),
    ),
    "CSU_C09_STUDY_SCHEDULE": (
        "sequence",
        (
            ["CSS", SEGMENTS["CSS"], (0, 1), "SEG"],
            ["CSU_C09_STUDY_OBSERVATION", None, (1, -1), "GRP"],
            ["CSU_C09_STUDY_PHARM", None, (1, -1), "GRP"],
        ),
    ),
    "CSU_C09_TIMING_QTY": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "CSU_C09_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "DFT_P03_COMMON_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (0, 1), "SEG"],
            ["DFT_P03_TIMING_QUANTITY", None, (0, -1), "GRP"],
            ["DFT_P03_ORDER", None, (0, 1), "GRP"],
            ["DFT_P03_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "DFT_P03_FINANCIAL": (
        "sequence",
        (
            ["FT1", SEGMENTS["FT1"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, 1), "SEG"],
            ["DFT_P03_FINANCIAL_PROCEDURE", None, (0, -1), "GRP"],
            ["DFT_P03_FINANCIAL_COMMON_ORDER", None, (0, -1), "GRP"],
        ),
    ),
    "DFT_P03_FINANCIAL_COMMON_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (0, 1), "SEG"],
            ["DFT_P03_FINANCIAL_TIMING_QUANTITY", None, (0, -1), "GRP"],
            ["DFT_P03_FINANCIAL_ORDER", None, (0, 1), "GRP"],
            ["DFT_P03_FINANCIAL_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "DFT_P03_FINANCIAL_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "DFT_P03_FINANCIAL_ORDER": (
        "sequence",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "DFT_P03_FINANCIAL_PROCEDURE": (
        "sequence",
        (
            ["PR1", SEGMENTS["PR1"], (1, 1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
        ),
    ),
    "DFT_P03_FINANCIAL_TIMING_QUANTITY": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "DFT_P03_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, -1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
        ),
    ),
    "DFT_P03_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "DFT_P03_ORDER": (
        "sequence",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "DFT_P03_TIMING_QUANTITY": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "DFT_P11_COMMON_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (0, 1), "SEG"],
            ["DFT_P11_TIMING_QUANTITY", None, (0, -1), "GRP"],
            ["DFT_P11_ORDER", None, (0, 1), "GRP"],
            ["DFT_P11_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "DFT_P11_FINANCIAL": (
        "sequence",
        (
            ["FT1", SEGMENTS["FT1"], (1, 1), "SEG"],
            ["DFT_P11_FINANCIAL_PROCEDURE", None, (0, -1), "GRP"],
            ["DFT_P11_FINANCIAL_COMMON_ORDER", None, (0, -1), "GRP"],
            ["DG1", SEGMENTS["DG1"], (0, -1), "SEG"],
            ["DRG", SEGMENTS["DRG"], (0, 1), "SEG"],
            ["GT1", SEGMENTS["GT1"], (0, -1), "SEG"],
            ["DFT_P11_FINANCIAL_INSURANCE", None, (0, -1), "GRP"],
        ),
    ),
    "DFT_P11_FINANCIAL_COMMON_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (0, 1), "SEG"],
            ["DFT_P11_FINANCIAL_TIMING_QUANTITY", None, (0, -1), "GRP"],
            ["DFT_P11_FINANCIAL_ORDER", None, (0, 1), "GRP"],
            ["DFT_P11_FINANCIAL_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "DFT_P11_FINANCIAL_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, -1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
        ),
    ),
    "DFT_P11_FINANCIAL_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "DFT_P11_FINANCIAL_ORDER": (
        "sequence",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "DFT_P11_FINANCIAL_PROCEDURE": (
        "sequence",
        (
            ["PR1", SEGMENTS["PR1"], (1, 1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
        ),
    ),
    "DFT_P11_FINANCIAL_TIMING_QUANTITY": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "DFT_P11_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, -1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
        ),
    ),
    "DFT_P11_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "DFT_P11_ORDER": (
        "sequence",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "DFT_P11_TIMING_QUANTITY": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "DOC_T12_RESULT": (
        "sequence",
        (
            ["EVN", SEGMENTS["EVN"], (0, 1), "SEG"],
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["TXA", SEGMENTS["TXA"], (1, 1), "SEG"],
            ["OBX", SEGMENTS["OBX"], (0, -1), "SEG"],
        ),
    ),
    "EAC_U07_COMMAND": (
        "sequence",
        (
            ["ECD", SEGMENTS["ECD"], (1, 1), "SEG"],
            ["TQ1", SEGMENTS["TQ1"], (0, 1), "SEG"],
            ["EAC_U07_SPECIMEN_CONTAINER", None, (0, 1), "GRP"],
            ["CNS", SEGMENTS["CNS"], (0, 1), "SEG"],
        ),
    ),
    "EAC_U07_SPECIMEN_CONTAINER": (
        "sequence",
        (
            ["SAC", SEGMENTS["SAC"], (1, 1), "SEG"],
            ["SPM", SEGMENTS["SPM"], (0, -1), "SEG"],
        ),
    ),
    "EAN_U09_NOTIFICATION": (
        "sequence",
        (
            ["NDS", SEGMENTS["NDS"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, 1), "SEG"],
        ),
    ),
    "EAR_U08_COMMAND_RESPONSE": (
        "sequence",
        (
            ["ECD", SEGMENTS["ECD"], (1, 1), "SEG"],
            ["EAR_U08_SPECIMEN_CONTAINER", None, (0, 1), "GRP"],
            ["ECR", SEGMENTS["ECR"], (1, 1), "SEG"],
        ),
    ),
    "EAR_U08_SPECIMEN_CONTAINER": (
        "sequence",
        (
            ["SAC", SEGMENTS["SAC"], (1, 1), "SEG"],
            ["SPM", SEGMENTS["SPM"], (0, -1), "SEG"],
        ),
    ),
    "MDM_T01_COMMON_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["MDM_T01_TIMING", None, (0, -1), "GRP"],
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "MDM_T01_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "MDM_T02_COMMON_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["MDM_T02_TIMING", None, (0, -1), "GRP"],
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "MDM_T02_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "MDM_T02_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "MFN_M01_MF": (
        "sequence",
        (
            ["MFE", SEGMENTS["MFE"], (1, 1), "SEG"],
            ["ANYHL7SEGMENT", SEGMENTS["ANYHL7SEGMENT"], (0, 1), "SEG"],
        ),
    ),
    "MFN_M02_MF_STAFF": (
        "sequence",
        (
            ["MFE", SEGMENTS["MFE"], (1, 1), "SEG"],
            ["STF", SEGMENTS["STF"], (1, 1), "SEG"],
            ["PRA", SEGMENTS["PRA"], (0, -1), "SEG"],
            ["ORG", SEGMENTS["ORG"], (0, -1), "SEG"],
            ["AFF", SEGMENTS["AFF"], (0, -1), "SEG"],
            ["LAN", SEGMENTS["LAN"], (0, -1), "SEG"],
            ["EDU", SEGMENTS["EDU"], (0, -1), "SEG"],
            ["CER", SEGMENTS["CER"], (0, -1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "MFN_M03_MF_TEST": (
        "sequence",
        (
            ["MFE", SEGMENTS["MFE"], (1, 1), "SEG"],
            ["OM1", SEGMENTS["OM1"], (1, 1), "SEG"],
            ["ANYHL7SEGMENT", SEGMENTS["ANYHL7SEGMENT"], (1, 1), "SEG"],
        ),
    ),
    "MFN_M04_MF_CDM": (
        "sequence",
        (
            ["MFE", SEGMENTS["MFE"], (1, 1), "SEG"],
            ["CDM", SEGMENTS["CDM"], (1, 1), "SEG"],
            ["PRC", SEGMENTS["PRC"], (0, -1), "SEG"],
        ),
    ),
    "MFN_M05_MF_LOCATION": (
        "sequence",
        (
            ["MFE", SEGMENTS["MFE"], (1, 1), "SEG"],
            ["LOC", SEGMENTS["LOC"], (1, 1), "SEG"],
            ["LCH", SEGMENTS["LCH"], (0, -1), "SEG"],
            ["LRL", SEGMENTS["LRL"], (0, -1), "SEG"],
            ["MFN_M05_MF_LOC_DEPT", None, (1, -1), "GRP"],
        ),
    ),
    "MFN_M05_MF_LOC_DEPT": (
        "sequence",
        (
            ["LDP", SEGMENTS["LDP"], (1, 1), "SEG"],
            ["LCH", SEGMENTS["LCH"], (0, -1), "SEG"],
            ["LCC", SEGMENTS["LCC"], (0, -1), "SEG"],
        ),
    ),
    "MFN_M06_MF_CLIN_STUDY": (
        "sequence",
        (
            ["MFE", SEGMENTS["MFE"], (1, 1), "SEG"],
            ["CM0", SEGMENTS["CM0"], (1, 1), "SEG"],
            ["MFN_M06_MF_PHASE_SCHED_DETAIL", None, (0, -1), "GRP"],
        ),
    ),
    "MFN_M06_MF_PHASE_SCHED_DETAIL": (
        "sequence",
        (
            ["CM1", SEGMENTS["CM1"], (1, 1), "SEG"],
            ["CM2", SEGMENTS["CM2"], (0, -1), "SEG"],
        ),
    ),
    "MFN_M07_MF_CLIN_STUDY_SCHED": (
        "sequence",
        (
            ["MFE", SEGMENTS["MFE"], (1, 1), "SEG"],
            ["CM0", SEGMENTS["CM0"], (1, 1), "SEG"],
            ["CM2", SEGMENTS["CM2"], (0, -1), "SEG"],
        ),
    ),
    "MFN_M08_MF_TEST_NUMERIC": (
        "sequence",
        (
            ["MFE", SEGMENTS["MFE"], (1, 1), "SEG"],
            ["OM1", SEGMENTS["OM1"], (1, 1), "SEG"],
            ["OM2", SEGMENTS["OM2"], (0, 1), "SEG"],
            ["OM3", SEGMENTS["OM3"], (0, 1), "SEG"],
            ["OM4", SEGMENTS["OM4"], (0, 1), "SEG"],
        ),
    ),
    "MFN_M09_MF_TEST_CATEGORICAL": (
        "sequence",
        (
            ["MFE", SEGMENTS["MFE"], (1, 1), "SEG"],
            ["OM1", SEGMENTS["OM1"], (1, 1), "SEG"],
            ["MFN_M09_MF_TEST_CAT_DETAIL", None, (0, 1), "GRP"],
        ),
    ),
    "MFN_M09_MF_TEST_CAT_DETAIL": (
        "sequence",
        (
            ["OM3", SEGMENTS["OM3"], (1, 1), "SEG"],
            ["OM4", SEGMENTS["OM4"], (0, -1), "SEG"],
        ),
    ),
    "MFN_M10_MF_TEST_BATTERIES": (
        "sequence",
        (
            ["MFE", SEGMENTS["MFE"], (1, 1), "SEG"],
            ["OM1", SEGMENTS["OM1"], (1, 1), "SEG"],
            ["MFN_M10_MF_TEST_BATT_DETAIL", None, (0, 1), "GRP"],
        ),
    ),
    "MFN_M10_MF_TEST_BATT_DETAIL": (
        "sequence",
        (
            ["OM5", SEGMENTS["OM5"], (1, 1), "SEG"],
            ["OM4", SEGMENTS["OM4"], (0, -1), "SEG"],
        ),
    ),
    "MFN_M11_MF_TEST_CALCULATED": (
        "sequence",
        (
            ["MFE", SEGMENTS["MFE"], (1, 1), "SEG"],
            ["OM1", SEGMENTS["OM1"], (1, 1), "SEG"],
            ["MFN_M11_MF_TEST_CALC_DETAIL", None, (0, 1), "GRP"],
        ),
    ),
    "MFN_M11_MF_TEST_CALC_DETAIL": (
        "sequence",
        (
            ["OM6", SEGMENTS["OM6"], (1, 1), "SEG"],
            ["OM2", SEGMENTS["OM2"], (1, 1), "SEG"],
        ),
    ),
    "MFN_M12_MF_OBS_ATTRIBUTES": (
        "sequence",
        (
            ["MFE", SEGMENTS["MFE"], (1, 1), "SEG"],
            ["OM1", SEGMENTS["OM1"], (1, 1), "SEG"],
            ["OM7", SEGMENTS["OM7"], (0, 1), "SEG"],
        ),
    ),
    "MFN_M15_MF_INV_ITEM": (
        "sequence",
        (
            ["MFE", SEGMENTS["MFE"], (1, 1), "SEG"],
            ["IIM", SEGMENTS["IIM"], (1, 1), "SEG"],
        ),
    ),
    "MFN_ZNN": (
        "sequence",
        (
            ["MSH", SEGMENTS["MSH"], (1, 1), "SEG"],
            ["SFT", SEGMENTS["SFT"], (0, -1), "SEG"],
            ["MFI", SEGMENTS["MFI"], (1, 1), "SEG"],
            ["MFN_ZNN_MF_SITE_DEFINED", None, (1, -1), "GRP"],
        ),
    ),
    "MFN_ZNN_MF_SITE_DEFINED": (
        "sequence",
        (
            ["MFE", SEGMENTS["MFE"], (1, 1), "SEG"],
            ["ANYHL7SEGMENT", SEGMENTS["ANYHL7SEGMENT"], (1, 1), "SEG"],
        ),
    ),
    "MFR_M01_MF_QUERY": (
        "sequence",
        (
            ["MFE", SEGMENTS["MFE"], (1, 1), "SEG"],
            ["ANYHL7SEGMENT", SEGMENTS["ANYHL7SEGMENT"], (0, 1), "SEG"],
        ),
    ),
    "MFR_M04_MF_QUERY": (
        "sequence",
        (
            ["MFE", SEGMENTS["MFE"], (1, 1), "SEG"],
            ["CDM", SEGMENTS["CDM"], (1, 1), "SEG"],
            ["LCH", SEGMENTS["LCH"], (0, -1), "SEG"],
            ["PRC", SEGMENTS["PRC"], (0, -1), "SEG"],
        ),
    ),
    "MFR_M05_MF_QUERY": (
        "sequence",
        (
            ["MFE", SEGMENTS["MFE"], (1, 1), "SEG"],
            ["LOC", SEGMENTS["LOC"], (1, 1), "SEG"],
            ["LCH", SEGMENTS["LCH"], (0, -1), "SEG"],
            ["LRL", SEGMENTS["LRL"], (0, -1), "SEG"],
            ["LDP", SEGMENTS["LDP"], (1, -1), "SEG"],
            ["LCH", SEGMENTS["LCH"], (0, -1), "SEG"],
            ["LCC", SEGMENTS["LCC"], (0, -1), "SEG"],
        ),
    ),
    "MFR_M06_MF_QUERY": (
        "sequence",
        (
            ["MFE", SEGMENTS["MFE"], (1, 1), "SEG"],
            ["CM0", SEGMENTS["CM0"], (1, 1), "SEG"],
            ["CM1", SEGMENTS["CM1"], (0, -1), "SEG"],
            ["CM2", SEGMENTS["CM2"], (0, -1), "SEG"],
        ),
    ),
    "MFR_M07_MF_QUERY": (
        "sequence",
        (
            ["MFE", SEGMENTS["MFE"], (1, 1), "SEG"],
            ["CM0", SEGMENTS["CM0"], (1, 1), "SEG"],
            ["CM2", SEGMENTS["CM2"], (0, -1), "SEG"],
        ),
    ),
    "NMD_N02_APP_STATS": (
        "sequence",
        (
            ["NST", SEGMENTS["NST"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "NMD_N02_APP_STATUS": (
        "sequence",
        (
            ["NSC", SEGMENTS["NSC"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "NMD_N02_CLOCK": (
        "sequence",
        (
            ["NCK", SEGMENTS["NCK"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "NMD_N02_CLOCK_AND_STATS_WITH_NOTES": (
        "sequence",
        (
            ["NMD_N02_CLOCK", None, (0, 1), "GRP"],
            ["NMD_N02_APP_STATS", None, (0, 1), "GRP"],
            ["NMD_N02_APP_STATUS", None, (0, 1), "GRP"],
        ),
    ),
    "NMQ_N01_CLOCK_AND_STATISTICS": (
        "sequence",
        (
            ["NCK", SEGMENTS["NCK"], (0, 1), "SEG"],
            ["NST", SEGMENTS["NST"], (0, 1), "SEG"],
            ["NSC", SEGMENTS["NSC"], (0, 1), "SEG"],
        ),
    ),
    "NMQ_N01_QRY_WITH_DETAIL": (
        "sequence",
        (
            ["QRD", SEGMENTS["QRD"], (1, 1), "SEG"],
            ["QRF", SEGMENTS["QRF"], (0, 1), "SEG"],
        ),
    ),
    "NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT": (
        "sequence",
        (
            ["NCK", SEGMENTS["NCK"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["NST", SEGMENTS["NST"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["NSC", SEGMENTS["NSC"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OMB_O27_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, 1), "SEG"],
        ),
    ),
    "OMB_O27_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OMB_O27_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["OMB_O27_TIMING", None, (0, -1), "GRP"],
            ["BPO", SEGMENTS["BPO"], (1, 1), "SEG"],
            ["SPM", SEGMENTS["SPM"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["DG1", SEGMENTS["DG1"], (0, -1), "SEG"],
            ["OMB_O27_OBSERVATION", None, (0, -1), "GRP"],
            ["FT1", SEGMENTS["FT1"], (0, -1), "SEG"],
            ["BLG", SEGMENTS["BLG"], (0, 1), "SEG"],
        ),
    ),
    "OMB_O27_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["OMB_O27_PATIENT_VISIT", None, (0, 1), "GRP"],
            ["OMB_O27_INSURANCE", None, (0, -1), "GRP"],
            ["GT1", SEGMENTS["GT1"], (0, 1), "SEG"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
        ),
    ),
    "OMB_O27_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "OMB_O27_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "OMD_O03_DIET": (
        "sequence",
        (
            ["ODS", SEGMENTS["ODS"], (1, -1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["OMD_O03_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "OMD_O03_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, 1), "SEG"],
        ),
    ),
    "OMD_O03_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OMD_O03_ORDER_DIET": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["OMD_O03_TIMING_DIET", None, (0, -1), "GRP"],
            ["OMD_O03_DIET", None, (0, 1), "GRP"],
        ),
    ),
    "OMD_O03_ORDER_TRAY": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["OMD_O03_TIMING_TRAY", None, (0, -1), "GRP"],
            ["ODT", SEGMENTS["ODT"], (1, -1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OMD_O03_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["OMD_O03_PATIENT_VISIT", None, (0, 1), "GRP"],
            ["OMD_O03_INSURANCE", None, (0, -1), "GRP"],
            ["GT1", SEGMENTS["GT1"], (0, 1), "SEG"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
        ),
    ),
    "OMD_O03_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "OMD_O03_TIMING_DIET": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "OMD_O03_TIMING_TRAY": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "OMG_O19_CONTAINER": (
        "sequence",
        (
            ["SAC", SEGMENTS["SAC"], (1, 1), "SEG"],
            ["OBX", SEGMENTS["OBX"], (0, -1), "SEG"],
        ),
    ),
    "OMG_O19_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, 1), "SEG"],
        ),
    ),
    "OMG_O19_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OMG_O19_OBSERVATION_PRIOR": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OMG_O19_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["OMG_O19_TIMING", None, (0, -1), "GRP"],
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, 1), "SEG"],
            ["DG1", SEGMENTS["DG1"], (0, -1), "SEG"],
            ["OMG_O19_OBSERVATION", None, (0, -1), "GRP"],
            ["OMG_O19_SPECIMEN", None, (0, -1), "GRP"],
            ["OMG_O19_PRIOR_RESULT", None, (0, -1), "GRP"],
            ["FT1", SEGMENTS["FT1"], (0, -1), "SEG"],
            ["CTI", SEGMENTS["CTI"], (0, -1), "SEG"],
            ["BLG", SEGMENTS["BLG"], (0, 1), "SEG"],
        ),
    ),
    "OMG_O19_ORDER_PRIOR": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (0, 1), "SEG"],
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["OMG_O19_TIMING_PRIOR", None, (0, -1), "GRP"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, 1), "SEG"],
            ["OMG_O19_OBSERVATION_PRIOR", None, (1, -1), "GRP"],
        ),
    ),
    "OMG_O19_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["NK1", SEGMENTS["NK1"], (0, -1), "SEG"],
            ["OMG_O19_PATIENT_VISIT", None, (0, 1), "GRP"],
            ["OMG_O19_INSURANCE", None, (0, -1), "GRP"],
            ["GT1", SEGMENTS["GT1"], (0, 1), "SEG"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
        ),
    ),
    "OMG_O19_PATIENT_PRIOR": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
        ),
    ),
    "OMG_O19_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "OMG_O19_PATIENT_VISIT_PRIOR": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "OMG_O19_PRIOR_RESULT": (
        "sequence",
        (
            ["OMG_O19_PATIENT_PRIOR", None, (0, 1), "GRP"],
            ["OMG_O19_PATIENT_VISIT_PRIOR", None, (0, 1), "GRP"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
            ["OMG_O19_ORDER_PRIOR", None, (1, -1), "GRP"],
        ),
    ),
    "OMG_O19_SPECIMEN": (
        "sequence",
        (
            ["SPM", SEGMENTS["SPM"], (1, 1), "SEG"],
            ["OBX", SEGMENTS["OBX"], (0, -1), "SEG"],
            ["OMG_O19_CONTAINER", None, (0, -1), "GRP"],
        ),
    ),
    "OMG_O19_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "OMG_O19_TIMING_PRIOR": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "OMI_O23_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, 1), "SEG"],
        ),
    ),
    "OMI_O23_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OMI_O23_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["OMI_O23_TIMING", None, (0, -1), "GRP"],
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, 1), "SEG"],
            ["DG1", SEGMENTS["DG1"], (0, -1), "SEG"],
            ["OMI_O23_OBSERVATION", None, (0, -1), "GRP"],
            ["IPC", SEGMENTS["IPC"], (1, -1), "SEG"],
        ),
    ),
    "OMI_O23_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["OMI_O23_PATIENT_VISIT", None, (0, 1), "GRP"],
            ["OMI_O23_INSURANCE", None, (0, -1), "GRP"],
            ["GT1", SEGMENTS["GT1"], (0, 1), "SEG"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
        ),
    ),
    "OMI_O23_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "OMI_O23_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "OML_O21_CONTAINER": (
        "sequence",
        (
            ["SAC", SEGMENTS["SAC"], (1, 1), "SEG"],
            ["OBX", SEGMENTS["OBX"], (0, -1), "SEG"],
        ),
    ),
    "OML_O21_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, 1), "SEG"],
        ),
    ),
    "OML_O21_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["TCD", SEGMENTS["TCD"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OML_O21_OBSERVATION_PRIOR": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OML_O21_OBSERVATION_REQUEST": (
        "sequence",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["TCD", SEGMENTS["TCD"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, 1), "SEG"],
            ["DG1", SEGMENTS["DG1"], (0, -1), "SEG"],
            ["OML_O21_OBSERVATION", None, (0, -1), "GRP"],
            ["OML_O21_SPECIMEN", None, (0, -1), "GRP"],
            ["OML_O21_PRIOR_RESULT", None, (0, -1), "GRP"],
        ),
    ),
    "OML_O21_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["OML_O21_TIIMING", None, (0, -1), "GRP"],
            ["OML_O21_OBSERVATION_REQUEST", None, (0, 1), "GRP"],
            ["FT1", SEGMENTS["FT1"], (0, -1), "SEG"],
            ["CTI", SEGMENTS["CTI"], (0, -1), "SEG"],
            ["BLG", SEGMENTS["BLG"], (0, 1), "SEG"],
        ),
    ),
    "OML_O21_ORDER_PRIOR": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (0, 1), "SEG"],
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["OML_O21_TIMING_PRIOR", None, (0, -1), "GRP"],
            ["OML_O21_OBSERVATION_PRIOR", None, (1, -1), "GRP"],
        ),
    ),
    "OML_O21_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["NK1", SEGMENTS["NK1"], (0, -1), "SEG"],
            ["OML_O21_PATIENT_VISIT", None, (0, 1), "GRP"],
            ["OML_O21_INSURANCE", None, (0, -1), "GRP"],
            ["GT1", SEGMENTS["GT1"], (0, 1), "SEG"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
        ),
    ),
    "OML_O21_PATIENT_PRIOR": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
        ),
    ),
    "OML_O21_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "OML_O21_PATIENT_VISIT_PRIOR": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "OML_O21_PRIOR_RESULT": (
        "sequence",
        (
            ["OML_O21_PATIENT_PRIOR", None, (0, 1), "GRP"],
            ["OML_O21_PATIENT_VISIT_PRIOR", None, (0, 1), "GRP"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
            ["OML_O21_ORDER_PRIOR", None, (1, -1), "GRP"],
        ),
    ),
    "OML_O21_SPECIMEN": (
        "sequence",
        (
            ["SPM", SEGMENTS["SPM"], (1, 1), "SEG"],
            ["OBX", SEGMENTS["OBX"], (0, -1), "SEG"],
            ["OML_O21_CONTAINER", None, (0, -1), "GRP"],
        ),
    ),
    "OML_O21_TIIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "OML_O21_TIMING_PRIOR": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "OML_O33_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, 1), "SEG"],
        ),
    ),
    "OML_O33_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["TCD", SEGMENTS["TCD"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OML_O33_OBSERVATION_PRIOR": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OML_O33_OBSERVATION_REQUEST": (
        "sequence",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["TCD", SEGMENTS["TCD"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["DG1", SEGMENTS["DG1"], (0, -1), "SEG"],
            ["OML_O33_OBSERVATION", None, (0, -1), "GRP"],
            ["OML_O33_PRIOR_RESULT", None, (0, -1), "GRP"],
        ),
    ),
    "OML_O33_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["OML_O33_TIMING", None, (0, -1), "GRP"],
            ["OML_O33_OBSERVATION_REQUEST", None, (0, 1), "GRP"],
            ["FT1", SEGMENTS["FT1"], (0, -1), "SEG"],
            ["CTI", SEGMENTS["CTI"], (0, -1), "SEG"],
            ["BLG", SEGMENTS["BLG"], (0, 1), "SEG"],
        ),
    ),
    "OML_O33_ORDER_PRIOR": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (0, 1), "SEG"],
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["OML_O33_TIMING_PRIOR", None, (0, -1), "GRP"],
            ["OML_O33_OBSERVATION_PRIOR", None, (1, -1), "GRP"],
        ),
    ),
    "OML_O33_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["NK1", SEGMENTS["NK1"], (0, -1), "SEG"],
            ["OML_O33_PATIENT_VISIT", None, (0, 1), "GRP"],
            ["OML_O33_INSURANCE", None, (0, -1), "GRP"],
            ["GT1", SEGMENTS["GT1"], (0, 1), "SEG"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
        ),
    ),
    "OML_O33_PATIENT_PRIOR": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
        ),
    ),
    "OML_O33_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "OML_O33_PATIENT_VISIT_PRIOR": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "OML_O33_PRIOR_RESULT": (
        "sequence",
        (
            ["OML_O33_PATIENT_PRIOR", None, (0, 1), "GRP"],
            ["OML_O33_PATIENT_VISIT_PRIOR", None, (0, 1), "GRP"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
            ["OML_O33_ORDER_PRIOR", None, (1, -1), "GRP"],
        ),
    ),
    "OML_O33_SPECIMEN": (
        "sequence",
        (
            ["SPM", SEGMENTS["SPM"], (1, 1), "SEG"],
            ["OBX", SEGMENTS["OBX"], (0, -1), "SEG"],
            ["SAC", SEGMENTS["SAC"], (0, -1), "SEG"],
            ["OML_O33_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "OML_O33_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "OML_O33_TIMING_PRIOR": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "OML_O35_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, 1), "SEG"],
        ),
    ),
    "OML_O35_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["TCD", SEGMENTS["TCD"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OML_O35_OBSERVATION_PRIOR": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OML_O35_OBSERVATION_REQUEST": (
        "sequence",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["TCD", SEGMENTS["TCD"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["DG1", SEGMENTS["DG1"], (0, -1), "SEG"],
            ["OML_O35_OBSERVATION", None, (0, -1), "GRP"],
            ["OML_O35_PRIOR_RESULT", None, (0, -1), "GRP"],
        ),
    ),
    "OML_O35_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["OML_O35_TIIMING", None, (0, -1), "GRP"],
            ["OML_O35_OBSERVATION_REQUEST", None, (0, 1), "GRP"],
            ["FT1", SEGMENTS["FT1"], (0, -1), "SEG"],
            ["CTI", SEGMENTS["CTI"], (0, -1), "SEG"],
            ["BLG", SEGMENTS["BLG"], (0, 1), "SEG"],
        ),
    ),
    "OML_O35_ORDER_PRIOR": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (0, 1), "SEG"],
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["OML_O35_TIMING_PRIOR", None, (0, -1), "GRP"],
            ["OML_O35_OBSERVATION_PRIOR", None, (1, -1), "GRP"],
        ),
    ),
    "OML_O35_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["NK1", SEGMENTS["NK1"], (0, -1), "SEG"],
            ["OML_O35_PATIENT_VISIT", None, (0, 1), "GRP"],
            ["OML_O35_INSURANCE", None, (0, -1), "GRP"],
            ["GT1", SEGMENTS["GT1"], (0, 1), "SEG"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
        ),
    ),
    "OML_O35_PATIENT_PRIOR": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
        ),
    ),
    "OML_O35_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "OML_O35_PATIENT_VISIT_PRIOR": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "OML_O35_PRIOR_RESULT": (
        "sequence",
        (
            ["OML_O35_PATIENT_PRIOR", None, (0, 1), "GRP"],
            ["OML_O35_PATIENT_VISIT_PRIOR", None, (0, 1), "GRP"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
            ["OML_O35_ORDER_PRIOR", None, (1, -1), "GRP"],
        ),
    ),
    "OML_O35_SPECIMEN": (
        "sequence",
        (
            ["SPM", SEGMENTS["SPM"], (1, 1), "SEG"],
            ["OBX", SEGMENTS["OBX"], (0, -1), "SEG"],
            ["OML_O35_SPECIMEN_CONTAINER", None, (1, -1), "GRP"],
        ),
    ),
    "OML_O35_SPECIMEN_CONTAINER": (
        "sequence",
        (
            ["SAC", SEGMENTS["SAC"], (1, 1), "SEG"],
            ["OML_O35_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "OML_O35_TIIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "OML_O35_TIMING_PRIOR": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "OMN_O07_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, 1), "SEG"],
        ),
    ),
    "OMN_O07_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OMN_O07_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["OMN_O07_TIMING", None, (0, -1), "GRP"],
            ["RQD", SEGMENTS["RQD"], (1, 1), "SEG"],
            ["RQ1", SEGMENTS["RQ1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["OMN_O07_OBSERVATION", None, (0, -1), "GRP"],
            ["BLG", SEGMENTS["BLG"], (0, 1), "SEG"],
        ),
    ),
    "OMN_O07_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["OMN_O07_PATIENT_VISIT", None, (0, 1), "GRP"],
            ["OMN_O07_INSURANCE", None, (0, -1), "GRP"],
            ["GT1", SEGMENTS["GT1"], (0, 1), "SEG"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
        ),
    ),
    "OMN_O07_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "OMN_O07_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "OMP_O09_COMPONENT": (
        "sequence",
        (
            ["RXC", SEGMENTS["RXC"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OMP_O09_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, 1), "SEG"],
        ),
    ),
    "OMP_O09_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OMP_O09_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["OMP_O09_TIMING", None, (0, -1), "GRP"],
            ["RXO", SEGMENTS["RXO"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["OMP_O09_COMPONENT", None, (0, -1), "GRP"],
            ["OMP_O09_OBSERVATION", None, (0, -1), "GRP"],
            ["FT1", SEGMENTS["FT1"], (0, -1), "SEG"],
            ["BLG", SEGMENTS["BLG"], (0, 1), "SEG"],
        ),
    ),
    "OMP_O09_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["OMP_O09_PATIENT_VISIT", None, (0, 1), "GRP"],
            ["OMP_O09_INSURANCE", None, (0, -1), "GRP"],
            ["GT1", SEGMENTS["GT1"], (0, 1), "SEG"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
        ),
    ),
    "OMP_O09_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "OMP_O09_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "OMS_O05_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, 1), "SEG"],
        ),
    ),
    "OMS_O05_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OMS_O05_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["OMS_O05_TIMING", None, (0, -1), "GRP"],
            ["RQD", SEGMENTS["RQD"], (1, 1), "SEG"],
            ["RQ1", SEGMENTS["RQ1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["OMS_O05_OBSERVATION", None, (0, -1), "GRP"],
            ["BLG", SEGMENTS["BLG"], (0, 1), "SEG"],
        ),
    ),
    "OMS_O05_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["OMS_O05_PATIENT_VISIT", None, (0, 1), "GRP"],
            ["OMS_O05_INSURANCE", None, (0, -1), "GRP"],
            ["GT1", SEGMENTS["GT1"], (0, 1), "SEG"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
        ),
    ),
    "OMS_O05_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "OMS_O05_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "ORB_O28_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["ORB_O28_TIMING", None, (0, -1), "GRP"],
            ["BPO", SEGMENTS["BPO"], (0, 1), "SEG"],
        ),
    ),
    "ORB_O28_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["ORB_O28_ORDER", None, (0, -1), "GRP"],
        ),
    ),
    "ORB_O28_RESPONSE": ("sequence", (["ORB_O28_PATIENT", None, (0, 1), "GRP"],)),
    "ORB_O28_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "ORD_O04_ORDER_DIET": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["ORD_O04_TIMING_DIET", None, (0, -1), "GRP"],
            ["ODS", SEGMENTS["ODS"], (0, -1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "ORD_O04_ORDER_TRAY": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["ORD_O04_TIMING_TRAY", None, (0, -1), "GRP"],
            ["ODT", SEGMENTS["ODT"], (0, -1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "ORD_O04_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "ORD_O04_RESPONSE": (
        "sequence",
        (
            ["ORD_O04_PATIENT", None, (0, 1), "GRP"],
            ["ORD_O04_ORDER_DIET", None, (1, -1), "GRP"],
            ["ORD_O04_ORDER_TRAY", None, (0, -1), "GRP"],
        ),
    ),
    "ORD_O04_TIMING_DIET": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "ORD_O04_TIMING_TRAY": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "ORF_R04_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "ORF_R04_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (0, 1), "SEG"],
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["ORF_R04_TIMING_QTY", None, (0, -1), "GRP"],
            ["CTD", SEGMENTS["CTD"], (0, 1), "SEG"],
            ["ORF_R04_OBSERVATION", None, (1, -1), "GRP"],
            ["CTI", SEGMENTS["CTI"], (0, -1), "SEG"],
        ),
    ),
    "ORF_R04_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "ORF_R04_QUERY_RESPONSE": (
        "sequence",
        (
            ["ORF_R04_PATIENT", None, (0, 1), "GRP"],
            ["ORF_R04_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "ORF_R04_TIMING_QTY": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "ORG_O20_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["ORG_O20_TIMING", None, (0, -1), "GRP"],
            ["OBR", SEGMENTS["OBR"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["CTI", SEGMENTS["CTI"], (0, -1), "SEG"],
            ["ORG_O20_SPECIMEN", None, (0, -1), "GRP"],
        ),
    ),
    "ORG_O20_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "ORG_O20_RESPONSE": (
        "sequence",
        (
            ["ORG_O20_PATIENT", None, (0, 1), "GRP"],
            ["ORG_O20_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "ORG_O20_SPECIMEN": (
        "sequence",
        (
            ["SPM", SEGMENTS["SPM"], (1, 1), "SEG"],
            ["SAC", SEGMENTS["SAC"], (0, -1), "SEG"],
        ),
    ),
    "ORG_O20_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "ORI_O24_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["ORI_O24_TIMING", None, (0, -1), "GRP"],
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["IPC", SEGMENTS["IPC"], (1, -1), "SEG"],
        ),
    ),
    "ORI_O24_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "ORI_O24_RESPONSE": (
        "sequence",
        (
            ["ORI_O24_PATIENT", None, (0, 1), "GRP"],
            ["ORI_O24_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "ORI_O24_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "ORL_O22_OBSERVATION_REQUEST": (
        "sequence",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["ORL_O22_SPECIMEN", None, (0, -1), "GRP"],
        ),
    ),
    "ORL_O22_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["ORL_O22_TIMING", None, (0, -1), "GRP"],
            ["ORL_O22_OBSERVATION_REQUEST", None, (0, 1), "GRP"],
        ),
    ),
    "ORL_O22_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["ORL_O22_ORDER", None, (0, -1), "GRP"],
        ),
    ),
    "ORL_O22_RESPONSE": ("sequence", (["ORL_O22_PATIENT", None, (0, 1), "GRP"],)),
    "ORL_O22_SPECIMEN": (
        "sequence",
        (
            ["SPM", SEGMENTS["SPM"], (1, 1), "SEG"],
            ["SAC", SEGMENTS["SAC"], (0, -1), "SEG"],
        ),
    ),
    "ORL_O22_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "ORL_O34_OBSERVATION_REQUEST": (
        "sequence",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["ORL_O34_SPMSAC_SUPPGRP2", None, (0, -1), "GRP"],
        ),
    ),
    "ORL_O34_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["ORL_O34_TIMING", None, (0, -1), "GRP"],
            ["ORL_O34_OBSERVATION_REQUEST", None, (0, 1), "GRP"],
        ),
    ),
    "ORL_O34_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["ORL_O34_SPECIMEN", None, (1, -1), "GRP"],
        ),
    ),
    "ORL_O34_RESPONSE": ("sequence", (["ORL_O34_PATIENT", None, (0, 1), "GRP"],)),
    "ORL_O34_SPECIMEN": (
        "sequence",
        (
            ["SPM", SEGMENTS["SPM"], (1, 1), "SEG"],
            ["OBX", SEGMENTS["OBX"], (0, -1), "SEG"],
            ["SAC", SEGMENTS["SAC"], (0, -1), "SEG"],
            ["ORL_O34_ORDER", None, (0, -1), "GRP"],
        ),
    ),
    "ORL_O34_SPMSAC_SUPPGRP2": (
        "sequence",
        (
            ["SPM", SEGMENTS["SPM"], (1, 1), "SEG"],
            ["SAC", SEGMENTS["SAC"], (0, -1), "SEG"],
        ),
    ),
    "ORL_O34_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "ORL_O36_OBSERVATION_REQUEST": (
        "sequence",
        (["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],),
    ),
    "ORL_O36_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["ORL_O36_TIMING", None, (0, -1), "GRP"],
            ["ORL_O36_OBSERVATION_REQUEST", None, (0, 1), "GRP"],
        ),
    ),
    "ORL_O36_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["ORL_O36_SPECIMEN", None, (1, -1), "GRP"],
        ),
    ),
    "ORL_O36_RESPONSE": ("sequence", (["ORL_O36_PATIENT", None, (0, 1), "GRP"],)),
    "ORL_O36_SPECIMEN": (
        "sequence",
        (
            ["SPM", SEGMENTS["SPM"], (1, 1), "SEG"],
            ["OBX", SEGMENTS["OBX"], (0, -1), "SEG"],
            ["ORL_O36_SPECIMEN_CONTAINER", None, (1, -1), "GRP"],
        ),
    ),
    "ORL_O36_SPECIMEN_CONTAINER": (
        "sequence",
        (
            ["SAC", SEGMENTS["SAC"], (1, 1), "SEG"],
            ["ORL_O36_ORDER", None, (0, -1), "GRP"],
        ),
    ),
    "ORL_O36_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "ORM_O01_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, 1), "SEG"],
        ),
    ),
    "ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP": (
        "choice",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["RQD", SEGMENTS["RQD"], (1, 1), "SEG"],
            ["RQ1", SEGMENTS["RQ1"], (1, 1), "SEG"],
            ["RXO", SEGMENTS["RXO"], (1, 1), "SEG"],
            ["ODS", SEGMENTS["ODS"], (1, 1), "SEG"],
            ["ODT", SEGMENTS["ODT"], (1, 1), "SEG"],
        ),
    ),
    "ORM_O01_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "ORM_O01_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["ORM_O01_ORDER_DETAIL", None, (0, 1), "GRP"],
            ["FT1", SEGMENTS["FT1"], (0, -1), "SEG"],
            ["CTI", SEGMENTS["CTI"], (0, -1), "SEG"],
            ["BLG", SEGMENTS["BLG"], (0, 1), "SEG"],
        ),
    ),
    "ORM_O01_ORDER_DETAIL": (
        "sequence",
        (
            ["ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP", None, (1, 1), "GRP"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, 1), "SEG"],
            ["DG1", SEGMENTS["DG1"], (0, -1), "SEG"],
            ["ORM_O01_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "ORM_O01_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["ORM_O01_PATIENT_VISIT", None, (0, 1), "GRP"],
            ["ORM_O01_INSURANCE", None, (0, -1), "GRP"],
            ["GT1", SEGMENTS["GT1"], (0, 1), "SEG"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
        ),
    ),
    "ORM_O01_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "ORN_O08_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["ORN_O08_TIMING", None, (0, -1), "GRP"],
            ["RQD", SEGMENTS["RQD"], (1, 1), "SEG"],
            ["RQ1", SEGMENTS["RQ1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "ORN_O08_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "ORN_O08_RESPONSE": (
        "sequence",
        (
            ["ORN_O08_PATIENT", None, (0, 1), "GRP"],
            ["ORN_O08_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "ORN_O08_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "ORP_O10_COMPONENT": (
        "sequence",
        (
            ["RXC", SEGMENTS["RXC"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "ORP_O10_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["ORP_O10_TIMING", None, (0, -1), "GRP"],
            ["ORP_O10_ORDER_DETAIL", None, (0, 1), "GRP"],
        ),
    ),
    "ORP_O10_ORDER_DETAIL": (
        "sequence",
        (
            ["RXO", SEGMENTS["RXO"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["ORP_O10_COMPONENT", None, (0, -1), "GRP"],
        ),
    ),
    "ORP_O10_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "ORP_O10_RESPONSE": (
        "sequence",
        (
            ["ORP_O10_PATIENT", None, (0, 1), "GRP"],
            ["ORP_O10_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "ORP_O10_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "ORR_O02_CHOICE": (
        "choice",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["RQD", SEGMENTS["RQD"], (1, 1), "SEG"],
            ["RQ1", SEGMENTS["RQ1"], (1, 1), "SEG"],
            ["RXO", SEGMENTS["RXO"], (1, 1), "SEG"],
            ["ODS", SEGMENTS["ODS"], (1, 1), "SEG"],
            ["ODT", SEGMENTS["ODT"], (1, 1), "SEG"],
        ),
    ),
    "ORR_O02_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["ORR_O02_CHOICE", None, (1, 1), "GRP"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["CTI", SEGMENTS["CTI"], (0, -1), "SEG"],
        ),
    ),
    "ORR_O02_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "ORR_O02_RESPONSE": (
        "sequence",
        (
            ["ORR_O02_PATIENT", None, (0, 1), "GRP"],
            ["ORR_O02_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "ORS_O06_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["ORS_O06_TIMING", None, (0, -1), "GRP"],
            ["RQD", SEGMENTS["RQD"], (1, 1), "SEG"],
            ["RQ1", SEGMENTS["RQ1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "ORS_O06_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "ORS_O06_RESPONSE": (
        "sequence",
        (
            ["ORS_O06_PATIENT", None, (0, 1), "GRP"],
            ["ORS_O06_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "ORS_O06_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "ORU_R01_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "ORU_R01_ORDER_OBSERVATION": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (0, 1), "SEG"],
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["ORU_R01_TIMING_QTY", None, (0, -1), "GRP"],
            ["CTD", SEGMENTS["CTD"], (0, 1), "SEG"],
            ["ORU_R01_OBSERVATION", None, (0, -1), "GRP"],
            ["FT1", SEGMENTS["FT1"], (0, -1), "SEG"],
            ["CTI", SEGMENTS["CTI"], (0, -1), "SEG"],
            ["ORU_R01_SPECIMEN", None, (0, -1), "GRP"],
        ),
    ),
    "ORU_R01_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["NK1", SEGMENTS["NK1"], (0, -1), "SEG"],
            ["ORU_R01_VISIT", None, (0, 1), "GRP"],
        ),
    ),
    "ORU_R01_PATIENT_RESULT": (
        "sequence",
        (
            ["ORU_R01_PATIENT", None, (0, 1), "GRP"],
            ["ORU_R01_ORDER_OBSERVATION", None, (1, -1), "GRP"],
        ),
    ),
    "ORU_R01_SPECIMEN": (
        "sequence",
        (
            ["SPM", SEGMENTS["SPM"], (1, 1), "SEG"],
            ["OBX", SEGMENTS["OBX"], (0, -1), "SEG"],
        ),
    ),
    "ORU_R01_TIMING_QTY": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "ORU_R01_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "ORU_R30_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "ORU_R30_TIMING_QTY": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "ORU_R30_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "OSR_Q06_CHOICE": (
        "choice",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["RQD", SEGMENTS["RQD"], (1, 1), "SEG"],
            ["RQ1", SEGMENTS["RQ1"], (1, 1), "SEG"],
            ["RXO", SEGMENTS["RXO"], (1, 1), "SEG"],
            ["ODS", SEGMENTS["ODS"], (1, 1), "SEG"],
            ["ODT", SEGMENTS["ODT"], (1, 1), "SEG"],
        ),
    ),
    "OSR_Q06_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["OSR_Q06_TIMING", None, (0, -1), "GRP"],
            ["OSR_Q06_CHOICE", None, (1, 1), "GRP"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["CTI", SEGMENTS["CTI"], (0, -1), "SEG"],
        ),
    ),
    "OSR_Q06_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OSR_Q06_RESPONSE": (
        "sequence",
        (
            ["OSR_Q06_PATIENT", None, (0, 1), "GRP"],
            ["OSR_Q06_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "OSR_Q06_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "OUL_R21_CONTAINER": (
        "sequence",
        (
            ["SAC", SEGMENTS["SAC"], (1, 1), "SEG"],
            ["SID", SEGMENTS["SID"], (0, 1), "SEG"],
        ),
    ),
    "OUL_R21_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (0, 1), "SEG"],
            ["TCD", SEGMENTS["TCD"], (0, 1), "SEG"],
            ["SID", SEGMENTS["SID"], (0, -1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OUL_R21_ORDER_OBSERVATION": (
        "sequence",
        (
            ["OUL_R21_CONTAINER", None, (0, 1), "GRP"],
            ["ORC", SEGMENTS["ORC"], (0, 1), "SEG"],
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["OUL_R21_TIMING_QTY", None, (0, -1), "GRP"],
            ["OUL_R21_OBSERVATION", None, (1, -1), "GRP"],
            ["CTI", SEGMENTS["CTI"], (0, -1), "SEG"],
        ),
    ),
    "OUL_R21_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OUL_R21_TIMING_QTY": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "OUL_R21_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "OUL_R22_CONTAINER": (
        "sequence",
        (
            ["SAC", SEGMENTS["SAC"], (1, 1), "SEG"],
            ["INV", SEGMENTS["INV"], (0, 1), "SEG"],
        ),
    ),
    "OUL_R22_ORDER": (
        "sequence",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["ORC", SEGMENTS["ORC"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["OUL_R22_TIMING_QTY", None, (0, -1), "GRP"],
            ["OUL_R22_RESULT", None, (0, -1), "GRP"],
            ["CTI", SEGMENTS["CTI"], (0, -1), "SEG"],
        ),
    ),
    "OUL_R22_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OUL_R22_RESULT": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["TCD", SEGMENTS["TCD"], (0, 1), "SEG"],
            ["SID", SEGMENTS["SID"], (0, -1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OUL_R22_SPECIMEN": (
        "sequence",
        (
            ["SPM", SEGMENTS["SPM"], (1, 1), "SEG"],
            ["OBX", SEGMENTS["OBX"], (0, -1), "SEG"],
            ["OUL_R22_CONTAINER", None, (0, -1), "GRP"],
            ["OUL_R22_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "OUL_R22_TIMING_QTY": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "OUL_R22_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "OUL_R23_CONTAINER": (
        "sequence",
        (
            ["SAC", SEGMENTS["SAC"], (1, 1), "SEG"],
            ["INV", SEGMENTS["INV"], (0, 1), "SEG"],
            ["OUL_R23_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "OUL_R23_ORDER": (
        "sequence",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["ORC", SEGMENTS["ORC"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["OUL_R23_TIMING_QTY", None, (0, -1), "GRP"],
            ["OUL_R23_RESULT", None, (0, -1), "GRP"],
            ["CTI", SEGMENTS["CTI"], (0, -1), "SEG"],
        ),
    ),
    "OUL_R23_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OUL_R23_RESULT": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["TCD", SEGMENTS["TCD"], (0, 1), "SEG"],
            ["SID", SEGMENTS["SID"], (0, -1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OUL_R23_SPECIMEN": (
        "sequence",
        (
            ["SPM", SEGMENTS["SPM"], (1, 1), "SEG"],
            ["OBX", SEGMENTS["OBX"], (0, -1), "SEG"],
            ["OUL_R23_CONTAINER", None, (1, -1), "GRP"],
        ),
    ),
    "OUL_R23_TIMING_QTY": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "OUL_R23_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "OUL_R24_CONTAINER": (
        "sequence",
        (
            ["SAC", SEGMENTS["SAC"], (1, 1), "SEG"],
            ["INV", SEGMENTS["INV"], (0, 1), "SEG"],
        ),
    ),
    "OUL_R24_ORDER": (
        "sequence",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["ORC", SEGMENTS["ORC"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["OUL_R24_TIMING_QTY", None, (0, -1), "GRP"],
            ["OUL_R24_SPECIMEN", None, (0, -1), "GRP"],
            ["OUL_R24_RESULT", None, (0, -1), "GRP"],
            ["CTI", SEGMENTS["CTI"], (0, -1), "SEG"],
        ),
    ),
    "OUL_R24_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OUL_R24_RESULT": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["TCD", SEGMENTS["TCD"], (0, 1), "SEG"],
            ["SID", SEGMENTS["SID"], (0, -1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "OUL_R24_SPECIMEN": (
        "sequence",
        (
            ["SPM", SEGMENTS["SPM"], (1, 1), "SEG"],
            ["OBX", SEGMENTS["OBX"], (0, -1), "SEG"],
            ["OUL_R24_CONTAINER", None, (0, -1), "GRP"],
        ),
    ),
    "OUL_R24_TIMING_QTY": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "OUL_R24_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "PEX_P07_ASSOCIATED_PERSON": (
        "sequence",
        (
            ["NK1", SEGMENTS["NK1"], (1, 1), "SEG"],
            ["PEX_P07_ASSOCIATED_RX_ORDER", None, (0, 1), "GRP"],
            ["PEX_P07_ASSOCIATED_RX_ADMIN", None, (0, -1), "GRP"],
            ["PRB", SEGMENTS["PRB"], (0, -1), "SEG"],
            ["OBX", SEGMENTS["OBX"], (0, -1), "SEG"],
        ),
    ),
    "PEX_P07_ASSOCIATED_RX_ADMIN": (
        "sequence",
        (
            ["RXA", SEGMENTS["RXA"], (1, 1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (0, 1), "SEG"],
        ),
    ),
    "PEX_P07_ASSOCIATED_RX_ORDER": (
        "sequence",
        (
            ["RXE", SEGMENTS["RXE"], (1, 1), "SEG"],
            ["PEX_P07_NK1_TIMING_QTY", None, (1, -1), "GRP"],
            ["RXR", SEGMENTS["RXR"], (0, -1), "SEG"],
        ),
    ),
    "PEX_P07_EXPERIENCE": (
        "sequence",
        (
            ["PES", SEGMENTS["PES"], (1, 1), "SEG"],
            ["PEX_P07_PEX_OBSERVATION", None, (1, -1), "GRP"],
        ),
    ),
    "PEX_P07_NK1_TIMING_QTY": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "PEX_P07_PEX_CAUSE": (
        "sequence",
        (
            ["PCR", SEGMENTS["PCR"], (1, 1), "SEG"],
            ["PEX_P07_RX_ORDER", None, (0, 1), "GRP"],
            ["PEX_P07_RX_ADMINISTRATION", None, (0, -1), "GRP"],
            ["PRB", SEGMENTS["PRB"], (0, -1), "SEG"],
            ["OBX", SEGMENTS["OBX"], (0, -1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["PEX_P07_ASSOCIATED_PERSON", None, (0, 1), "GRP"],
            ["PEX_P07_STUDY", None, (0, -1), "GRP"],
        ),
    ),
    "PEX_P07_PEX_OBSERVATION": (
        "sequence",
        (
            ["PEO", SEGMENTS["PEO"], (1, 1), "SEG"],
            ["PEX_P07_PEX_CAUSE", None, (1, -1), "GRP"],
        ),
    ),
    "PEX_P07_RX_ADMINISTRATION": (
        "sequence",
        (
            ["RXA", SEGMENTS["RXA"], (1, 1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (0, 1), "SEG"],
        ),
    ),
    "PEX_P07_RX_ORDER": (
        "sequence",
        (
            ["RXE", SEGMENTS["RXE"], (1, 1), "SEG"],
            ["PEX_P07_TIMING_QTY", None, (1, -1), "GRP"],
            ["RXR", SEGMENTS["RXR"], (0, -1), "SEG"],
        ),
    ),
    "PEX_P07_STUDY": (
        "sequence",
        (
            ["CSR", SEGMENTS["CSR"], (1, 1), "SEG"],
            ["CSP", SEGMENTS["CSP"], (0, -1), "SEG"],
        ),
    ),
    "PEX_P07_TIMING_QTY": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "PEX_P07_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "PGL_PC6_CHOICE": (
        "choice",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["ANYHL7SEGMENT", SEGMENTS["ANYHL7SEGMENT"], (1, 1), "SEG"],
        ),
    ),
    "PGL_PC6_GOAL": (
        "sequence",
        (
            ["GOL", SEGMENTS["GOL"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PGL_PC6_GOAL_ROLE", None, (0, -1), "GRP"],
            ["PGL_PC6_PATHWAY", None, (0, -1), "GRP"],
            ["PGL_PC6_OBSERVATION", None, (0, -1), "GRP"],
            ["PGL_PC6_PROBLEM", None, (0, -1), "GRP"],
            ["PGL_PC6_ORDER", None, (0, -1), "GRP"],
        ),
    ),
    "PGL_PC6_GOAL_ROLE": (
        "sequence",
        (
            ["ROL", SEGMENTS["ROL"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PGL_PC6_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "PGL_PC6_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["PGL_PC6_ORDER_DETAIL", None, (0, 1), "GRP"],
        ),
    ),
    "PGL_PC6_ORDER_DETAIL": (
        "sequence",
        (
            ["PGL_PC6_CHOICE", None, (1, 1), "GRP"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PGL_PC6_ORDER_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "PGL_PC6_ORDER_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PGL_PC6_PATHWAY": (
        "sequence",
        (
            ["PTH", SEGMENTS["PTH"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PGL_PC6_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "PGL_PC6_PROBLEM": (
        "sequence",
        (
            ["PRB", SEGMENTS["PRB"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PGL_PC6_PROBLEM_ROLE", None, (0, -1), "GRP"],
            ["PGL_PC6_PROBLEM_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "PGL_PC6_PROBLEM_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "PGL_PC6_PROBLEM_ROLE": (
        "sequence",
        (
            ["ROL", SEGMENTS["ROL"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PMU_B07_CERTIFICATE": (
        "sequence",
        (
            ["CER", SEGMENTS["CER"], (1, 1), "SEG"],
            ["ROL", SEGMENTS["ROL"], (0, -1), "SEG"],
        ),
    ),
    "PPG_PCG_CHOICE": (
        "choice",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["ANYHL7SEGMENT", SEGMENTS["ANYHL7SEGMENT"], (1, 1), "SEG"],
        ),
    ),
    "PPG_PCG_GOAL": (
        "sequence",
        (
            ["GOL", SEGMENTS["GOL"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PPG_PCG_GOAL_ROLE", None, (0, -1), "GRP"],
            ["PPG_PCG_GOAL_OBSERVATION", None, (0, -1), "GRP"],
            ["PPG_PCG_PROBLEM", None, (0, -1), "GRP"],
            ["PPG_PCG_ORDER", None, (0, -1), "GRP"],
        ),
    ),
    "PPG_PCG_GOAL_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "PPG_PCG_GOAL_ROLE": (
        "sequence",
        (
            ["ROL", SEGMENTS["ROL"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PPG_PCG_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["PPG_PCG_ORDER_DETAIL", None, (0, 1), "GRP"],
        ),
    ),
    "PPG_PCG_ORDER_DETAIL": (
        "sequence",
        (
            ["PPG_PCG_CHOICE", None, (1, 1), "GRP"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PPG_PCG_ORDER_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "PPG_PCG_ORDER_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PPG_PCG_PATHWAY": (
        "sequence",
        (
            ["PTH", SEGMENTS["PTH"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PPG_PCG_PATHWAY_ROLE", None, (0, -1), "GRP"],
            ["PPG_PCG_GOAL", None, (0, -1), "GRP"],
        ),
    ),
    "PPG_PCG_PATHWAY_ROLE": (
        "sequence",
        (
            ["ROL", SEGMENTS["ROL"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PPG_PCG_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "PPG_PCG_PROBLEM": (
        "sequence",
        (
            ["PRB", SEGMENTS["PRB"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PPG_PCG_PROBLEM_ROLE", None, (0, -1), "GRP"],
            ["PPG_PCG_PROBLEM_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "PPG_PCG_PROBLEM_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "PPG_PCG_PROBLEM_ROLE": (
        "sequence",
        (
            ["ROL", SEGMENTS["ROL"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PPP_PCB_CHOICE": (
        "choice",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["ANYHL7SEGMENT", SEGMENTS["ANYHL7SEGMENT"], (1, 1), "SEG"],
        ),
    ),
    "PPP_PCB_GOAL": (
        "sequence",
        (
            ["GOL", SEGMENTS["GOL"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PPP_PCB_GOAL_ROLE", None, (0, -1), "GRP"],
            ["PPP_PCB_GOAL_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "PPP_PCB_GOAL_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "PPP_PCB_GOAL_ROLE": (
        "sequence",
        (
            ["ROL", SEGMENTS["ROL"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PPP_PCB_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["PPP_PCB_ORDER_DETAIL", None, (0, 1), "GRP"],
        ),
    ),
    "PPP_PCB_ORDER_DETAIL": (
        "sequence",
        (
            ["PPP_PCB_CHOICE", None, (1, 1), "GRP"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PPP_PCB_ORDER_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "PPP_PCB_ORDER_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PPP_PCB_PATHWAY": (
        "sequence",
        (
            ["PTH", SEGMENTS["PTH"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PPP_PCB_PATHWAY_ROLE", None, (0, -1), "GRP"],
            ["PPP_PCB_PROBLEM", None, (0, -1), "GRP"],
        ),
    ),
    "PPP_PCB_PATHWAY_ROLE": (
        "sequence",
        (
            ["ROL", SEGMENTS["ROL"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PPP_PCB_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "PPP_PCB_PROBLEM": (
        "sequence",
        (
            ["PRB", SEGMENTS["PRB"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PPP_PCB_PROBLEM_ROLE", None, (0, -1), "GRP"],
            ["PPP_PCB_PROBLEM_OBSERVATION", None, (0, -1), "GRP"],
            ["PPP_PCB_GOAL", None, (0, -1), "GRP"],
            ["PPP_PCB_ORDER", None, (0, -1), "GRP"],
        ),
    ),
    "PPP_PCB_PROBLEM_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "PPP_PCB_PROBLEM_ROLE": (
        "sequence",
        (
            ["ROL", SEGMENTS["ROL"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PPR_PC1_CHOICE": (
        "choice",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["ANYHL7SEGMENT", SEGMENTS["ANYHL7SEGMENT"], (1, 1), "SEG"],
        ),
    ),
    "PPR_PC1_GOAL": (
        "sequence",
        (
            ["GOL", SEGMENTS["GOL"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PPR_PC1_GOAL_ROLE", None, (0, -1), "GRP"],
            ["PPR_PC1_GOAL_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "PPR_PC1_GOAL_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "PPR_PC1_GOAL_ROLE": (
        "sequence",
        (
            ["ROL", SEGMENTS["ROL"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PPR_PC1_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["PPR_PC1_ORDER_DETAIL", None, (0, 1), "GRP"],
        ),
    ),
    "PPR_PC1_ORDER_DETAIL": (
        "sequence",
        (
            ["PPR_PC1_CHOICE", None, (1, 1), "GRP"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PPR_PC1_ORDER_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "PPR_PC1_ORDER_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PPR_PC1_PATHWAY": (
        "sequence",
        (
            ["PTH", SEGMENTS["PTH"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PPR_PC1_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "PPR_PC1_PROBLEM": (
        "sequence",
        (
            ["PRB", SEGMENTS["PRB"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PPR_PC1_PROBLEM_ROLE", None, (0, -1), "GRP"],
            ["PPR_PC1_PATHWAY", None, (0, -1), "GRP"],
            ["PPR_PC1_PROBLEM_OBSERVATION", None, (0, -1), "GRP"],
            ["PPR_PC1_GOAL", None, (0, -1), "GRP"],
            ["PPR_PC1_ORDER", None, (0, -1), "GRP"],
        ),
    ),
    "PPR_PC1_PROBLEM_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "PPR_PC1_PROBLEM_ROLE": (
        "sequence",
        (
            ["ROL", SEGMENTS["ROL"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PPT_PCL_CHOICE": (
        "choice",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["ANYHL7SEGMENT", SEGMENTS["ANYHL7SEGMENT"], (1, 1), "SEG"],
        ),
    ),
    "PPT_PCL_GOAL": (
        "sequence",
        (
            ["GOL", SEGMENTS["GOL"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PPT_PCL_GOAL_ROLE", None, (0, -1), "GRP"],
            ["PPT_PCL_GOAL_OBSERVATION", None, (0, -1), "GRP"],
            ["PPT_PCL_PROBLEM", None, (0, -1), "GRP"],
            ["PPT_PCL_ORDER", None, (0, -1), "GRP"],
        ),
    ),
    "PPT_PCL_GOAL_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "PPT_PCL_GOAL_ROLE": (
        "sequence",
        (
            ["ROL", SEGMENTS["ROL"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PPT_PCL_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["PPT_PCL_ORDER_DETAIL", None, (0, 1), "GRP"],
        ),
    ),
    "PPT_PCL_ORDER_DETAIL": (
        "sequence",
        (
            ["PPT_PCL_CHOICE", None, (1, 1), "GRP"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PPT_PCL_ORDER_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "PPT_PCL_ORDER_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PPT_PCL_PATHWAY": (
        "sequence",
        (
            ["PTH", SEGMENTS["PTH"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PPT_PCL_PATHWAY_ROLE", None, (0, -1), "GRP"],
            ["PPT_PCL_GOAL", None, (0, -1), "GRP"],
        ),
    ),
    "PPT_PCL_PATHWAY_ROLE": (
        "sequence",
        (
            ["ROL", SEGMENTS["ROL"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PPT_PCL_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PPT_PCL_PATIENT_VISIT", None, (0, 1), "GRP"],
            ["PPT_PCL_PATHWAY", None, (1, -1), "GRP"],
        ),
    ),
    "PPT_PCL_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "PPT_PCL_PROBLEM": (
        "sequence",
        (
            ["PRB", SEGMENTS["PRB"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PPT_PCL_PROBLEM_ROLE", None, (0, -1), "GRP"],
            ["PPT_PCL_PROBLEM_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "PPT_PCL_PROBLEM_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "PPT_PCL_PROBLEM_ROLE": (
        "sequence",
        (
            ["ROL", SEGMENTS["ROL"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PPV_PCA_GOAL": (
        "sequence",
        (
            ["GOL", SEGMENTS["GOL"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PPV_PCA_GOAL_ROLE", None, (0, -1), "GRP"],
            ["PPV_PCA_GOAL_PATHWAY", None, (0, -1), "GRP"],
            ["PPV_PCA_GOAL_OBSERVATION", None, (0, -1), "GRP"],
            ["PPV_PCA_PROBLEM", None, (0, -1), "GRP"],
            ["PPV_PCA_ORDER", None, (0, -1), "GRP"],
        ),
    ),
    "PPV_PCA_GOAL_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "PPV_PCA_GOAL_PATHWAY": (
        "sequence",
        (
            ["PTH", SEGMENTS["PTH"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PPV_PCA_GOAL_ROLE": (
        "sequence",
        (
            ["ROL", SEGMENTS["ROL"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PPV_PCA_OBRANYHL7SEGMENT_SUPPGRP": (
        "choice",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["ANYHL7SEGMENT", SEGMENTS["ANYHL7SEGMENT"], (1, 1), "SEG"],
        ),
    ),
    "PPV_PCA_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["PPV_PCA_ORDER_DETAIL", None, (0, 1), "GRP"],
        ),
    ),
    "PPV_PCA_ORDER_DETAIL": (
        "sequence",
        (
            ["PPV_PCA_OBRANYHL7SEGMENT_SUPPGRP", None, (1, 1), "GRP"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PPV_PCA_ORDER_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "PPV_PCA_ORDER_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PPV_PCA_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PPV_PCA_PATIENT_VISIT", None, (0, 1), "GRP"],
            ["PPV_PCA_GOAL", None, (1, -1), "GRP"],
        ),
    ),
    "PPV_PCA_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "PPV_PCA_PROBLEM": (
        "sequence",
        (
            ["PRB", SEGMENTS["PRB"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PPV_PCA_PROBLEM_ROLE", None, (0, -1), "GRP"],
            ["PPV_PCA_PROBLEM_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "PPV_PCA_PROBLEM_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "PPV_PCA_PROBLEM_ROLE": (
        "sequence",
        (
            ["ROL", SEGMENTS["ROL"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PRR_PC5_CHOICE": (
        "choice",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["ANYHL7SEGMENT", SEGMENTS["ANYHL7SEGMENT"], (1, 1), "SEG"],
        ),
    ),
    "PRR_PC5_GOAL": (
        "sequence",
        (
            ["GOL", SEGMENTS["GOL"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PRR_PC5_GOAL_ROLE", None, (0, -1), "GRP"],
            ["PRR_PC5_GOAL_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "PRR_PC5_GOAL_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "PRR_PC5_GOAL_ROLE": (
        "sequence",
        (
            ["ROL", SEGMENTS["ROL"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PRR_PC5_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["PRR_PC5_ORDER_DETAIL", None, (0, 1), "GRP"],
        ),
    ),
    "PRR_PC5_ORDER_DETAIL": (
        "sequence",
        (
            ["PRR_PC5_CHOICE", None, (1, 1), "GRP"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PRR_PC5_ORDER_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "PRR_PC5_ORDER_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PRR_PC5_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PRR_PC5_PATIENT_VISIT", None, (0, 1), "GRP"],
            ["PRR_PC5_PROBLEM", None, (1, -1), "GRP"],
        ),
    ),
    "PRR_PC5_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "PRR_PC5_PROBLEM": (
        "sequence",
        (
            ["PRB", SEGMENTS["PRB"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PRR_PC5_PROBLEM_ROLE", None, (0, -1), "GRP"],
            ["PRR_PC5_PROBLEM_PATHWAY", None, (0, -1), "GRP"],
            ["PRR_PC5_PROBLEM_OBSERVATION", None, (0, -1), "GRP"],
            ["PRR_PC5_GOAL", None, (0, -1), "GRP"],
            ["PRR_PC5_ORDER", None, (0, -1), "GRP"],
        ),
    ),
    "PRR_PC5_PROBLEM_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "PRR_PC5_PROBLEM_PATHWAY": (
        "sequence",
        (
            ["PTH", SEGMENTS["PTH"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PRR_PC5_PROBLEM_ROLE": (
        "sequence",
        (
            ["ROL", SEGMENTS["ROL"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PTR_PCF_CHOICE": (
        "choice",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["ANYHL7SEGMENT", SEGMENTS["ANYHL7SEGMENT"], (1, 1), "SEG"],
        ),
    ),
    "PTR_PCF_GOAL": (
        "sequence",
        (
            ["GOL", SEGMENTS["GOL"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PTR_PCF_GOAL_ROLE", None, (0, -1), "GRP"],
            ["PTR_PCF_GOAL_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "PTR_PCF_GOAL_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "PTR_PCF_GOAL_ROLE": (
        "sequence",
        (
            ["ROL", SEGMENTS["ROL"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PTR_PCF_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["PTR_PCF_ORDER_DETAIL", None, (0, 1), "GRP"],
        ),
    ),
    "PTR_PCF_ORDER_DETAIL": (
        "sequence",
        (
            ["PTR_PCF_CHOICE", None, (1, 1), "GRP"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PTR_PCF_ORDER_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "PTR_PCF_ORDER_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PTR_PCF_PATHWAY": (
        "sequence",
        (
            ["PTH", SEGMENTS["PTH"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PTR_PCF_PATHWAY_ROLE", None, (0, -1), "GRP"],
            ["PTR_PCF_PROBLEM", None, (0, -1), "GRP"],
        ),
    ),
    "PTR_PCF_PATHWAY_ROLE": (
        "sequence",
        (
            ["ROL", SEGMENTS["ROL"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "PTR_PCF_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PTR_PCF_PATIENT_VISIT", None, (0, 1), "GRP"],
            ["PTR_PCF_PATHWAY", None, (1, -1), "GRP"],
        ),
    ),
    "PTR_PCF_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "PTR_PCF_PROBLEM": (
        "sequence",
        (
            ["PRB", SEGMENTS["PRB"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
            ["PTR_PCF_PROBLEM_ROLE", None, (0, -1), "GRP"],
            ["PTR_PCF_PROBLEM_OBSERVATION", None, (0, -1), "GRP"],
            ["PTR_PCF_GOAL", None, (0, -1), "GRP"],
            ["PTR_PCF_ORDER", None, (0, -1), "GRP"],
        ),
    ),
    "PTR_PCF_PROBLEM_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "PTR_PCF_PROBLEM_ROLE": (
        "sequence",
        (
            ["ROL", SEGMENTS["ROL"], (1, 1), "SEG"],
            ["VAR", SEGMENTS["VAR"], (0, -1), "SEG"],
        ),
    ),
    "QBP_K13_ROW_DEFINITION": (
        "sequence",
        (
            ["RDF", SEGMENTS["RDF"], (1, 1), "SEG"],
            ["RDT", SEGMENTS["RDT"], (0, -1), "SEG"],
        ),
    ),
    "QBP_QNN": (
        "sequence",
        (
            ["MSH", SEGMENTS["MSH"], (1, 1), "SEG"],
            ["SFT", SEGMENTS["SFT"], (0, -1), "SEG"],
            ["QPD", SEGMENTS["QPD"], (1, 1), "SEG"],
            ["RDF", SEGMENTS["RDF"], (0, 1), "SEG"],
            ["RCP", SEGMENTS["RCP"], (1, 1), "SEG"],
            ["DSC", SEGMENTS["DSC"], (0, 1), "SEG"],
        ),
    ),
    "QVR_Q17_QBP": (
        "sequence",
        (["ANYHL7SEGMENT", SEGMENTS["ANYHL7SEGMENT"], (0, 1), "SEG"],),
    ),
    "RAR_RAR_DEFINITION": (
        "sequence",
        (
            ["QRD", SEGMENTS["QRD"], (1, 1), "SEG"],
            ["QRF", SEGMENTS["QRF"], (0, 1), "SEG"],
            ["RAR_RAR_PATIENT", None, (0, 1), "GRP"],
            ["RAR_RAR_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "RAR_RAR_ENCODING": (
        "sequence",
        (
            ["RXE", SEGMENTS["RXE"], (1, 1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
        ),
    ),
    "RAR_RAR_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["RAR_RAR_ENCODING", None, (0, 1), "GRP"],
            ["RXA", SEGMENTS["RXA"], (1, -1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, 1), "SEG"],
        ),
    ),
    "RAR_RAR_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RAS_O17_ADMINISTRATION": (
        "sequence",
        (
            ["RXA", SEGMENTS["RXA"], (1, -1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, 1), "SEG"],
            ["RAS_O17_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "RAS_O17_COMPONENTS": (
        "sequence",
        (
            ["RXC", SEGMENTS["RXC"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RAS_O17_ENCODING": (
        "sequence",
        (
            ["RXE", SEGMENTS["RXE"], (1, 1), "SEG"],
            ["RAS_O17_TIMING_ENCODED", None, (1, -1), "GRP"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
        ),
    ),
    "RAS_O17_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RAS_O17_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["RAS_O17_TIMING", None, (0, -1), "GRP"],
            ["RAS_O17_ORDER_DETAIL", None, (0, 1), "GRP"],
            ["RAS_O17_ENCODING", None, (0, 1), "GRP"],
            ["RAS_O17_ADMINISTRATION", None, (1, -1), "GRP"],
            ["CTI", SEGMENTS["CTI"], (0, -1), "SEG"],
        ),
    ),
    "RAS_O17_ORDER_DETAIL": (
        "sequence",
        (
            ["RXO", SEGMENTS["RXO"], (1, 1), "SEG"],
            ["RAS_O17_ORDER_DETAIL_SUPPLEMENT", None, (0, 1), "GRP"],
        ),
    ),
    "RAS_O17_ORDER_DETAIL_SUPPLEMENT": (
        "sequence",
        (
            ["NTE", SEGMENTS["NTE"], (1, -1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RAS_O17_COMPONENTS", None, (0, -1), "GRP"],
        ),
    ),
    "RAS_O17_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
            ["RAS_O17_PATIENT_VISIT", None, (0, 1), "GRP"],
        ),
    ),
    "RAS_O17_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "RAS_O17_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "RAS_O17_TIMING_ENCODED": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "RCI_I05_OBSERVATION": (
        "sequence",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["RCI_I05_RESULTS", None, (0, -1), "GRP"],
        ),
    ),
    "RCI_I05_PROVIDER": (
        "sequence",
        (
            ["PRD", SEGMENTS["PRD"], (1, 1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, -1), "SEG"],
        ),
    ),
    "RCI_I05_RESULTS": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RCL_I06_PROVIDER": (
        "sequence",
        (
            ["PRD", SEGMENTS["PRD"], (1, 1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, -1), "SEG"],
        ),
    ),
    "RDE_O11_COMPONENT": (
        "sequence",
        (
            ["RXC", SEGMENTS["RXC"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RDE_O11_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, 1), "SEG"],
        ),
    ),
    "RDE_O11_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RDE_O11_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["RDE_O11_TIMING", None, (0, -1), "GRP"],
            ["RDE_O11_ORDER_DETAIL", None, (0, 1), "GRP"],
            ["RXE", SEGMENTS["RXE"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["RDE_O11_TIMING_ENCODED", None, (1, -1), "GRP"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
            ["RDE_O11_OBSERVATION", None, (0, -1), "GRP"],
            ["FT1", SEGMENTS["FT1"], (0, -1), "SEG"],
            ["BLG", SEGMENTS["BLG"], (0, 1), "SEG"],
            ["CTI", SEGMENTS["CTI"], (0, -1), "SEG"],
        ),
    ),
    "RDE_O11_ORDER_DETAIL": (
        "sequence",
        (
            ["RXO", SEGMENTS["RXO"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RDE_O11_COMPONENT", None, (0, -1), "GRP"],
        ),
    ),
    "RDE_O11_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["RDE_O11_PATIENT_VISIT", None, (0, 1), "GRP"],
            ["RDE_O11_INSURANCE", None, (0, -1), "GRP"],
            ["GT1", SEGMENTS["GT1"], (0, 1), "SEG"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
        ),
    ),
    "RDE_O11_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "RDE_O11_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "RDE_O11_TIMING_ENCODED": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "RDR_RDR_DEFINITION": (
        "sequence",
        (
            ["QRD", SEGMENTS["QRD"], (1, 1), "SEG"],
            ["QRF", SEGMENTS["QRF"], (0, 1), "SEG"],
            ["RDR_RDR_PATIENT", None, (0, 1), "GRP"],
            ["RDR_RDR_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "RDR_RDR_DISPENSE": (
        "sequence",
        (
            ["RXD", SEGMENTS["RXD"], (1, 1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
        ),
    ),
    "RDR_RDR_ENCODING": (
        "sequence",
        (
            ["RXE", SEGMENTS["RXE"], (1, 1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
        ),
    ),
    "RDR_RDR_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["RDR_RDR_ENCODING", None, (0, 1), "GRP"],
            ["RDR_RDR_DISPENSE", None, (1, -1), "GRP"],
        ),
    ),
    "RDR_RDR_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RDS_O13_COMPONENT": (
        "sequence",
        (
            ["RXC", SEGMENTS["RXC"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RDS_O13_ENCODING": (
        "sequence",
        (
            ["RXE", SEGMENTS["RXE"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["RDS_O13_TIMING_ENCODED", None, (1, -1), "GRP"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
        ),
    ),
    "RDS_O13_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RDS_O13_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["RDS_O13_TIMING", None, (0, -1), "GRP"],
            ["RDS_O13_ORDER_DETAIL", None, (0, 1), "GRP"],
            ["RDS_O13_ENCODING", None, (0, 1), "GRP"],
            ["RXD", SEGMENTS["RXD"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
            ["RDS_O13_OBSERVATION", None, (0, -1), "GRP"],
            ["FT1", SEGMENTS["FT1"], (0, -1), "SEG"],
        ),
    ),
    "RDS_O13_ORDER_DETAIL": (
        "sequence",
        (
            ["RXO", SEGMENTS["RXO"], (1, 1), "SEG"],
            ["RDS_O13_ORDER_DETAIL_SUPPLEMENT", None, (0, 1), "GRP"],
        ),
    ),
    "RDS_O13_ORDER_DETAIL_SUPPLEMENT": (
        "sequence",
        (
            ["NTE", SEGMENTS["NTE"], (1, -1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RDS_O13_COMPONENT", None, (0, -1), "GRP"],
        ),
    ),
    "RDS_O13_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
            ["RDS_O13_PATIENT_VISIT", None, (0, 1), "GRP"],
        ),
    ),
    "RDS_O13_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "RDS_O13_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "RDS_O13_TIMING_ENCODED": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "REF_I12_AUTCTD_SUPPGRP2": (
        "sequence",
        (
            ["AUT", SEGMENTS["AUT"], (1, 1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, 1), "SEG"],
        ),
    ),
    "REF_I12_AUTHORIZATION_CONTACT": (
        "sequence",
        (
            ["AUT", SEGMENTS["AUT"], (1, 1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, 1), "SEG"],
        ),
    ),
    "REF_I12_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, 1), "SEG"],
        ),
    ),
    "REF_I12_OBSERVATION": (
        "sequence",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["REF_I12_RESULTS_NOTES", None, (0, -1), "GRP"],
        ),
    ),
    "REF_I12_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "REF_I12_PROCEDURE": (
        "sequence",
        (
            ["PR1", SEGMENTS["PR1"], (1, 1), "SEG"],
            ["REF_I12_AUTCTD_SUPPGRP2", None, (0, 1), "GRP"],
        ),
    ),
    "REF_I12_PROVIDER_CONTACT": (
        "sequence",
        (
            ["PRD", SEGMENTS["PRD"], (1, 1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, -1), "SEG"],
        ),
    ),
    "REF_I12_RESULTS_NOTES": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RER_RER_DEFINITION": (
        "sequence",
        (
            ["QRD", SEGMENTS["QRD"], (1, 1), "SEG"],
            ["QRF", SEGMENTS["QRF"], (0, 1), "SEG"],
            ["RER_RER_PATIENT", None, (0, 1), "GRP"],
            ["RER_RER_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "RER_RER_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["RXE", SEGMENTS["RXE"], (1, 1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
        ),
    ),
    "RER_RER_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RGR_RGR_DEFINITION": (
        "sequence",
        (
            ["QRD", SEGMENTS["QRD"], (1, 1), "SEG"],
            ["QRF", SEGMENTS["QRF"], (0, 1), "SEG"],
            ["RGR_RGR_PATIENT", None, (0, 1), "GRP"],
            ["RGR_RGR_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "RGR_RGR_ENCODING": (
        "sequence",
        (
            ["RXE", SEGMENTS["RXE"], (1, 1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
        ),
    ),
    "RGR_RGR_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["RGR_RGR_ENCODING", None, (0, 1), "GRP"],
            ["RXG", SEGMENTS["RXG"], (1, -1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
        ),
    ),
    "RGR_RGR_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RGV_O15_COMPONENTS": (
        "sequence",
        (
            ["RXC", SEGMENTS["RXC"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RGV_O15_ENCODING": (
        "sequence",
        (
            ["RXE", SEGMENTS["RXE"], (1, 1), "SEG"],
            ["RGV_O15_TIMING_ENCODED", None, (1, -1), "GRP"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
        ),
    ),
    "RGV_O15_GIVE": (
        "sequence",
        (
            ["RXG", SEGMENTS["RXG"], (1, 1), "SEG"],
            ["RGV_O15_TIMING_GIVE", None, (1, -1), "GRP"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
            ["RGV_O15_OBSERVATION", None, (1, -1), "GRP"],
        ),
    ),
    "RGV_O15_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RGV_O15_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["RGV_O15_TIMING", None, (0, -1), "GRP"],
            ["RGV_O15_ORDER_DETAIL", None, (0, 1), "GRP"],
            ["RGV_O15_ENCODING", None, (0, 1), "GRP"],
            ["RGV_O15_GIVE", None, (1, -1), "GRP"],
        ),
    ),
    "RGV_O15_ORDER_DETAIL": (
        "sequence",
        (
            ["RXO", SEGMENTS["RXO"], (1, 1), "SEG"],
            ["RGV_O15_ORDER_DETAIL_SUPPLEMENT", None, (0, 1), "GRP"],
        ),
    ),
    "RGV_O15_ORDER_DETAIL_SUPPLEMENT": (
        "sequence",
        (
            ["NTE", SEGMENTS["NTE"], (1, -1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RGV_O15_COMPONENTS", None, (0, -1), "GRP"],
        ),
    ),
    "RGV_O15_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
            ["RGV_O15_PATIENT_VISIT", None, (0, 1), "GRP"],
        ),
    ),
    "RGV_O15_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "RGV_O15_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "RGV_O15_TIMING_ENCODED": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "RGV_O15_TIMING_GIVE": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "ROR_ROR_DEFINITION": (
        "sequence",
        (
            ["QRD", SEGMENTS["QRD"], (1, 1), "SEG"],
            ["QRF", SEGMENTS["QRF"], (0, 1), "SEG"],
            ["ROR_ROR_PATIENT", None, (0, 1), "GRP"],
            ["ROR_ROR_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "ROR_ROR_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["RXO", SEGMENTS["RXO"], (1, 1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
        ),
    ),
    "ROR_ROR_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RPA_I08_AUTHORIZATION_1": (
        "sequence",
        (
            ["AUT", SEGMENTS["AUT"], (1, 1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, 1), "SEG"],
        ),
    ),
    "RPA_I08_AUTHORIZATION_2": (
        "sequence",
        (
            ["AUT", SEGMENTS["AUT"], (1, 1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, 1), "SEG"],
        ),
    ),
    "RPA_I08_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, 1), "SEG"],
        ),
    ),
    "RPA_I08_OBSERVATION": (
        "sequence",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["RPA_I08_RESULTS", None, (0, -1), "GRP"],
        ),
    ),
    "RPA_I08_PROCEDURE": (
        "sequence",
        (
            ["PR1", SEGMENTS["PR1"], (1, 1), "SEG"],
            ["RPA_I08_AUTHORIZATION_2", None, (0, 1), "GRP"],
        ),
    ),
    "RPA_I08_PROVIDER": (
        "sequence",
        (
            ["PRD", SEGMENTS["PRD"], (1, 1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, -1), "SEG"],
        ),
    ),
    "RPA_I08_RESULTS": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RPA_I08_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "RPI_I01_GUARANTOR_INSURANCE": (
        "sequence",
        (
            ["GT1", SEGMENTS["GT1"], (0, -1), "SEG"],
            ["RPI_I01_INSURANCE", None, (1, -1), "GRP"],
        ),
    ),
    "RPI_I01_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, 1), "SEG"],
        ),
    ),
    "RPI_I01_PROVIDER": (
        "sequence",
        (
            ["PRD", SEGMENTS["PRD"], (1, 1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, -1), "SEG"],
        ),
    ),
    "RPI_I04_GUARANTOR_INSURANCE": (
        "sequence",
        (
            ["GT1", SEGMENTS["GT1"], (0, -1), "SEG"],
            ["RPI_I04_INSURANCE", None, (1, -1), "GRP"],
        ),
    ),
    "RPI_I04_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, 1), "SEG"],
        ),
    ),
    "RPI_I04_PROVIDER": (
        "sequence",
        (
            ["PRD", SEGMENTS["PRD"], (1, 1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, -1), "SEG"],
        ),
    ),
    "RPL_I02_PROVIDER": (
        "sequence",
        (
            ["PRD", SEGMENTS["PRD"], (1, 1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, -1), "SEG"],
        ),
    ),
    "RPR_I03_PROVIDER": (
        "sequence",
        (
            ["PRD", SEGMENTS["PRD"], (1, 1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, -1), "SEG"],
        ),
    ),
    "RQA_I08_AUTCTD_SUPPGRP2": (
        "sequence",
        (
            ["AUT", SEGMENTS["AUT"], (1, 1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, 1), "SEG"],
        ),
    ),
    "RQA_I08_AUTHORIZATION": (
        "sequence",
        (
            ["AUT", SEGMENTS["AUT"], (1, 1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, 1), "SEG"],
        ),
    ),
    "RQA_I08_GUARANTOR_INSURANCE": (
        "sequence",
        (
            ["GT1", SEGMENTS["GT1"], (0, -1), "SEG"],
            ["RQA_I08_INSURANCE", None, (1, -1), "GRP"],
        ),
    ),
    "RQA_I08_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, 1), "SEG"],
        ),
    ),
    "RQA_I08_OBSERVATION": (
        "sequence",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["RQA_I08_RESULTS", None, (0, -1), "GRP"],
        ),
    ),
    "RQA_I08_PROCEDURE": (
        "sequence",
        (
            ["PR1", SEGMENTS["PR1"], (1, 1), "SEG"],
            ["RQA_I08_AUTCTD_SUPPGRP2", None, (0, 1), "GRP"],
        ),
    ),
    "RQA_I08_PROVIDER": (
        "sequence",
        (
            ["PRD", SEGMENTS["PRD"], (1, 1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, -1), "SEG"],
        ),
    ),
    "RQA_I08_RESULTS": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RQA_I08_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "RQC_I05_PROVIDER": (
        "sequence",
        (
            ["PRD", SEGMENTS["PRD"], (1, 1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, -1), "SEG"],
        ),
    ),
    "RQI_I01_GUARANTOR_INSURANCE": (
        "sequence",
        (
            ["GT1", SEGMENTS["GT1"], (0, -1), "SEG"],
            ["RQI_I01_INSURANCE", None, (1, -1), "GRP"],
        ),
    ),
    "RQI_I01_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, 1), "SEG"],
        ),
    ),
    "RQI_I01_PROVIDER": (
        "sequence",
        (
            ["PRD", SEGMENTS["PRD"], (1, 1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, -1), "SEG"],
        ),
    ),
    "RQP_I04_PROVIDER": (
        "sequence",
        (
            ["PRD", SEGMENTS["PRD"], (1, 1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, -1), "SEG"],
        ),
    ),
    "RRA_O18_ADMINISTRATION": (
        "sequence",
        (
            ["RXA", SEGMENTS["RXA"], (1, -1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, 1), "SEG"],
        ),
    ),
    "RRA_O18_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["RRA_O18_TIMING", None, (0, -1), "GRP"],
            ["RRA_O18_ADMINISTRATION", None, (0, 1), "GRP"],
        ),
    ),
    "RRA_O18_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RRA_O18_RESPONSE": (
        "sequence",
        (
            ["RRA_O18_PATIENT", None, (0, 1), "GRP"],
            ["RRA_O18_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "RRA_O18_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "RRD_O14_DISPENSE": (
        "sequence",
        (
            ["RXD", SEGMENTS["RXD"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
        ),
    ),
    "RRD_O14_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["RRD_O14_TIMING", None, (0, -1), "GRP"],
            ["RRD_O14_DISPENSE", None, (0, 1), "GRP"],
        ),
    ),
    "RRD_O14_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RRD_O14_RESPONSE": (
        "sequence",
        (
            ["RRD_O14_PATIENT", None, (0, 1), "GRP"],
            ["RRD_O14_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "RRD_O14_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "RRE_O12_ENCODING": (
        "sequence",
        (
            ["RXE", SEGMENTS["RXE"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["RRE_O12_TIMING_ENCODED", None, (1, -1), "GRP"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
        ),
    ),
    "RRE_O12_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["RRE_O12_TIMING", None, (0, -1), "GRP"],
            ["RRE_O12_ENCODING", None, (0, 1), "GRP"],
        ),
    ),
    "RRE_O12_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RRE_O12_RESPONSE": (
        "sequence",
        (
            ["RRE_O12_PATIENT", None, (0, 1), "GRP"],
            ["RRE_O12_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "RRE_O12_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "RRE_O12_TIMING_ENCODED": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "RRG_O16_GIVE": (
        "sequence",
        (
            ["RXG", SEGMENTS["RXG"], (1, 1), "SEG"],
            ["RRG_O16_TIMING_GIVE", None, (1, -1), "GRP"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
        ),
    ),
    "RRG_O16_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["RRG_O16_TIMING", None, (0, -1), "GRP"],
            ["RRG_O16_GIVE", None, (0, 1), "GRP"],
        ),
    ),
    "RRG_O16_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RRG_O16_RESPONSE": (
        "sequence",
        (
            ["RRG_O16_PATIENT", None, (0, 1), "GRP"],
            ["RRG_O16_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "RRG_O16_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "RRG_O16_TIMING_GIVE": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "RRI_I12_AUTCTD_SUPPGRP2": (
        "sequence",
        (
            ["AUT", SEGMENTS["AUT"], (1, 1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, 1), "SEG"],
        ),
    ),
    "RRI_I12_AUTHORIZATION_CONTACT": (
        "sequence",
        (
            ["AUT", SEGMENTS["AUT"], (1, 1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, 1), "SEG"],
        ),
    ),
    "RRI_I12_OBSERVATION": (
        "sequence",
        (
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["RRI_I12_RESULTS_NOTES", None, (0, -1), "GRP"],
        ),
    ),
    "RRI_I12_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "RRI_I12_PROCEDURE": (
        "sequence",
        (
            ["PR1", SEGMENTS["PR1"], (1, 1), "SEG"],
            ["RRI_I12_AUTCTD_SUPPGRP2", None, (0, 1), "GRP"],
        ),
    ),
    "RRI_I12_PROVIDER_CONTACT": (
        "sequence",
        (
            ["PRD", SEGMENTS["PRD"], (1, 1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, -1), "SEG"],
        ),
    ),
    "RRI_I12_RESULTS_NOTES": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RSP_K11_ROW_DEFINITION": (
        "sequence",
        (
            ["RDF", SEGMENTS["RDF"], (1, 1), "SEG"],
            ["RDT", SEGMENTS["RDT"], (0, -1), "SEG"],
        ),
    ),
    "RSP_K21_QUERY_RESPONSE": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NK1", SEGMENTS["NK1"], (0, -1), "SEG"],
            ["QRI", SEGMENTS["QRI"], (1, 1), "SEG"],
        ),
    ),
    "RSP_K23_QUERY_RESPONSE": ("sequence", (["PID", SEGMENTS["PID"], (1, 1), "SEG"],)),
    "RSP_K25_STAFF": (
        "sequence",
        (
            ["STF", SEGMENTS["STF"], (1, 1), "SEG"],
            ["PRA", SEGMENTS["PRA"], (0, -1), "SEG"],
            ["ORG", SEGMENTS["ORG"], (0, -1), "SEG"],
            ["AFF", SEGMENTS["AFF"], (0, -1), "SEG"],
            ["LAN", SEGMENTS["LAN"], (0, -1), "SEG"],
            ["EDU", SEGMENTS["EDU"], (0, -1), "SEG"],
            ["CER", SEGMENTS["CER"], (0, -1), "SEG"],
        ),
    ),
    "RSP_K31_COMPONENTS": (
        "sequence",
        (
            ["RXC", SEGMENTS["RXC"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RSP_K31_ENCODING": (
        "sequence",
        (
            ["RXE", SEGMENTS["RXE"], (1, 1), "SEG"],
            ["RSP_K31_TIMING_ENCODED", None, (1, -1), "GRP"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
        ),
    ),
    "RSP_K31_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RSP_K31_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["RSP_K31_TIMING", None, (0, -1), "GRP"],
            ["RSP_K31_ORDER_DETAIL", None, (0, 1), "GRP"],
            ["RSP_K31_ENCODING", None, (0, 1), "GRP"],
            ["RXD", SEGMENTS["RXD"], (1, 1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
            ["RSP_K31_OBSERVATION", None, (1, -1), "GRP"],
        ),
    ),
    "RSP_K31_ORDER_DETAIL": (
        "sequence",
        (
            ["RXO", SEGMENTS["RXO"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RSP_K31_COMPONENTS", None, (0, -1), "GRP"],
        ),
    ),
    "RSP_K31_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
            ["RSP_K31_PATIENT_VISIT", None, (0, 1), "GRP"],
        ),
    ),
    "RSP_K31_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "RSP_K31_RESPONSE": (
        "sequence",
        (
            ["RSP_K31_PATIENT", None, (0, 1), "GRP"],
            ["RSP_K31_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "RSP_K31_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "RSP_K31_TIMING_ENCODED": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Q11_MF_LOC_DEPT": (
        "sequence",
        (
            ["LDP", SEGMENTS["LDP"], (1, 1), "SEG"],
            ["LCH", SEGMENTS["LCH"], (0, -1), "SEG"],
            ["LCC", SEGMENTS["LCC"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Q11_QUERY_RESULT_CLUSTER": (
        "sequence",
        (
            ["MFE", SEGMENTS["MFE"], (1, 1), "SEG"],
            ["LOC", SEGMENTS["LOC"], (1, 1), "SEG"],
            ["LCH", SEGMENTS["LCH"], (0, -1), "SEG"],
            ["LRL", SEGMENTS["LRL"], (0, -1), "SEG"],
            ["RSP_Q11_MF_LOC_DEPT", None, (1, -1), "GRP"],
        ),
    ),
    "RSP_Z82_COMMON_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["RSP_Z82_TIMING", None, (0, -1), "GRP"],
            ["RSP_Z82_ORDER_DETAIL", None, (0, 1), "GRP"],
            ["RSP_Z82_ENCODED_ORDER", None, (0, 1), "GRP"],
            ["RXD", SEGMENTS["RXD"], (1, 1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
            ["RSP_Z82_OBSERVATION", None, (1, -1), "GRP"],
        ),
    ),
    "RSP_Z82_ENCODED_ORDER": (
        "sequence",
        (
            ["RXE", SEGMENTS["RXE"], (1, 1), "SEG"],
            ["RSP_Z82_TIMING_ENCODED", None, (0, -1), "GRP"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Z82_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Z82_ORDER_DETAIL": (
        "sequence",
        (
            ["RXO", SEGMENTS["RXO"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RSP_Z82_TREATMENT", None, (0, 1), "GRP"],
        ),
    ),
    "RSP_Z82_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["RSP_Z82_VISIT", None, (0, 1), "GRP"],
        ),
    ),
    "RSP_Z82_QUERY_RESPONSE": (
        "sequence",
        (
            ["RSP_Z82_PATIENT", None, (0, 1), "GRP"],
            ["RSP_Z82_COMMON_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "RSP_Z82_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Z82_TIMING_ENCODED": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Z82_TREATMENT": (
        "sequence",
        (
            ["RXC", SEGMENTS["RXC"], (1, -1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Z82_VISIT": (
        "sequence",
        (
            ["AL1", SEGMENTS["AL1"], (1, -1), "SEG"],
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "RSP_Z86_ADMINISTRATION": (
        "sequence",
        (
            ["RXA", SEGMENTS["RXA"], (1, 1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Z86_COMMON_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["RSP_Z86_TIMING", None, (0, -1), "GRP"],
            ["RSP_Z86_ORDER_DETAIL", None, (0, 1), "GRP"],
            ["RSP_Z86_ENCODED_ORDER", None, (0, 1), "GRP"],
            ["RSP_Z86_DISPENSE", None, (0, 1), "GRP"],
            ["RSP_Z86_GIVE", None, (0, 1), "GRP"],
            ["RSP_Z86_ADMINISTRATION", None, (0, 1), "GRP"],
            ["RSP_Z86_OBSERVATION", None, (1, -1), "GRP"],
        ),
    ),
    "RSP_Z86_DISPENSE": (
        "sequence",
        (
            ["RXD", SEGMENTS["RXD"], (1, 1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Z86_ENCODED_ORDER": (
        "sequence",
        (
            ["RXE", SEGMENTS["RXE"], (1, 1), "SEG"],
            ["RSP_Z86_TIMING_ENCODED", None, (0, -1), "GRP"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Z86_GIVE": (
        "sequence",
        (
            ["RXG", SEGMENTS["RXG"], (1, 1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Z86_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Z86_ORDER_DETAIL": (
        "sequence",
        (
            ["RXO", SEGMENTS["RXO"], (1, 1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Z86_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["AL1", SEGMENTS["AL1"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Z86_QUERY_RESPONSE": (
        "sequence",
        (
            ["RSP_Z86_PATIENT", None, (0, 1), "GRP"],
            ["RSP_Z86_COMMON_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "RSP_Z86_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Z86_TIMING_ENCODED": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Z88_ALLERGY": (
        "sequence",
        (
            ["AL1", SEGMENTS["AL1"], (1, -1), "SEG"],
            ["RSP_Z88_VISIT", None, (0, 1), "GRP"],
        ),
    ),
    "RSP_Z88_COMMON_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["RSP_Z88_TIMING", None, (0, -1), "GRP"],
            ["RSP_Z88_ORDER_DETAIL", None, (0, 1), "GRP"],
            ["RSP_Z88_ORDER_ENCODED", None, (0, 1), "GRP"],
            ["RXD", SEGMENTS["RXD"], (1, 1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
            ["RSP_Z88_OBSERVATION", None, (1, -1), "GRP"],
        ),
    ),
    "RSP_Z88_COMPONENT": (
        "sequence",
        (
            ["RXC", SEGMENTS["RXC"], (1, -1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Z88_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Z88_ORDER_DETAIL": (
        "sequence",
        (
            ["RXO", SEGMENTS["RXO"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RSP_Z88_COMPONENT", None, (0, 1), "GRP"],
        ),
    ),
    "RSP_Z88_ORDER_ENCODED": (
        "sequence",
        (
            ["RXE", SEGMENTS["RXE"], (1, 1), "SEG"],
            ["RSP_Z88_TIMING_ENCODED", None, (0, -1), "GRP"],
            ["RXR", SEGMENTS["RXR"], (1, -1), "SEG"],
            ["RXC", SEGMENTS["RXC"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Z88_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["RSP_Z88_ALLERGY", None, (0, 1), "GRP"],
        ),
    ),
    "RSP_Z88_QUERY_RESPONSE": (
        "sequence",
        (
            ["RSP_Z88_PATIENT", None, (0, 1), "GRP"],
            ["RSP_Z88_COMMON_ORDER", None, (1, -1), "GRP"],
        ),
    ),
    "RSP_Z88_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Z88_TIMING_ENCODED": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Z88_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "RSP_Z90_COMMON_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["RSP_Z90_TIMING", None, (0, -1), "GRP"],
            ["OBR", SEGMENTS["OBR"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["CTD", SEGMENTS["CTD"], (0, 1), "SEG"],
            ["RSP_Z90_OBSERVATION", None, (1, -1), "GRP"],
        ),
    ),
    "RSP_Z90_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Z90_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["NK1", SEGMENTS["NK1"], (0, -1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["RSP_Z90_VISIT", None, (0, 1), "GRP"],
        ),
    ),
    "RSP_Z90_QUERY_RESPONSE": (
        "sequence",
        (
            ["RSP_Z90_PATIENT", None, (0, 1), "GRP"],
            ["RSP_Z90_COMMON_ORDER", None, (1, -1), "GRP"],
            ["RSP_Z90_SPECIMEN", None, (0, -1), "GRP"],
        ),
    ),
    "RSP_Z90_SPECIMEN": (
        "sequence",
        (
            ["SPM", SEGMENTS["SPM"], (1, 1), "SEG"],
            ["OBX", SEGMENTS["OBX"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Z90_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "RSP_Z90_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "RTB_K13_ROW_DEFINITION": (
        "sequence",
        (
            ["RDF", SEGMENTS["RDF"], (1, 1), "SEG"],
            ["RDT", SEGMENTS["RDT"], (0, -1), "SEG"],
        ),
    ),
    "RTB_KNN": (
        "sequence",
        (
            ["MSH", SEGMENTS["MSH"], (1, 1), "SEG"],
            ["SFT", SEGMENTS["SFT"], (0, -1), "SEG"],
            ["MSA", SEGMENTS["MSA"], (1, 1), "SEG"],
            ["ERR", SEGMENTS["ERR"], (0, 1), "SEG"],
            ["QAK", SEGMENTS["QAK"], (1, 1), "SEG"],
            ["QPD", SEGMENTS["QPD"], (1, 1), "SEG"],
            ["ANYHL7SEGMENT", SEGMENTS["ANYHL7SEGMENT"], (1, 1), "SEG"],
            ["ANYHL7SEGMENT", SEGMENTS["ANYHL7SEGMENT"], (1, 1), "SEG"],
            ["DSC", SEGMENTS["DSC"], (0, 1), "SEG"],
        ),
    ),
    "RTB_Z74_ROW_DEFINITION": (
        "sequence",
        (
            ["RDF", SEGMENTS["RDF"], (1, 1), "SEG"],
            ["RDT", SEGMENTS["RDT"], (0, -1), "SEG"],
        ),
    ),
    "SIU_S12_GENERAL_RESOURCE": (
        "sequence",
        (
            ["AIG", SEGMENTS["AIG"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "SIU_S12_LOCATION_RESOURCE": (
        "sequence",
        (
            ["AIL", SEGMENTS["AIL"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "SIU_S12_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PD1", SEGMENTS["PD1"], (0, 1), "SEG"],
            ["PV1", SEGMENTS["PV1"], (0, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
            ["OBX", SEGMENTS["OBX"], (0, -1), "SEG"],
            ["DG1", SEGMENTS["DG1"], (0, -1), "SEG"],
        ),
    ),
    "SIU_S12_PERSONNEL_RESOURCE": (
        "sequence",
        (
            ["AIP", SEGMENTS["AIP"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "SIU_S12_RESOURCES": (
        "sequence",
        (
            ["RGS", SEGMENTS["RGS"], (1, 1), "SEG"],
            ["SIU_S12_SERVICE", None, (0, -1), "GRP"],
            ["SIU_S12_GENERAL_RESOURCE", None, (0, -1), "GRP"],
            ["SIU_S12_LOCATION_RESOURCE", None, (0, -1), "GRP"],
            ["SIU_S12_PERSONNEL_RESOURCE", None, (0, -1), "GRP"],
        ),
    ),
    "SIU_S12_SERVICE": (
        "sequence",
        (
            ["AIS", SEGMENTS["AIS"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "SQM_S25_GENERAL_RESOURCE": (
        "sequence",
        (
            ["AIG", SEGMENTS["AIG"], (1, 1), "SEG"],
            ["APR", SEGMENTS["APR"], (0, 1), "SEG"],
        ),
    ),
    "SQM_S25_LOCATION_RESOURCE": (
        "sequence",
        (
            ["AIL", SEGMENTS["AIL"], (1, 1), "SEG"],
            ["APR", SEGMENTS["APR"], (0, 1), "SEG"],
        ),
    ),
    "SQM_S25_PERSONNEL_RESOURCE": (
        "sequence",
        (
            ["AIP", SEGMENTS["AIP"], (1, 1), "SEG"],
            ["APR", SEGMENTS["APR"], (0, 1), "SEG"],
        ),
    ),
    "SQM_S25_REQUEST": (
        "sequence",
        (
            ["ARQ", SEGMENTS["ARQ"], (1, 1), "SEG"],
            ["APR", SEGMENTS["APR"], (0, 1), "SEG"],
            ["PID", SEGMENTS["PID"], (0, 1), "SEG"],
            ["SQM_S25_RESOURCES", None, (1, -1), "GRP"],
        ),
    ),
    "SQM_S25_RESOURCES": (
        "sequence",
        (
            ["RGS", SEGMENTS["RGS"], (1, 1), "SEG"],
            ["SQM_S25_SERVICE", None, (0, -1), "GRP"],
            ["SQM_S25_GENERAL_RESOURCE", None, (0, -1), "GRP"],
            ["SQM_S25_PERSONNEL_RESOURCE", None, (0, -1), "GRP"],
            ["SQM_S25_LOCATION_RESOURCE", None, (0, -1), "GRP"],
        ),
    ),
    "SQM_S25_SERVICE": (
        "sequence",
        (
            ["AIS", SEGMENTS["AIS"], (1, 1), "SEG"],
            ["APR", SEGMENTS["APR"], (0, 1), "SEG"],
        ),
    ),
    "SQR_S25_GENERAL_RESOURCE": (
        "sequence",
        (
            ["AIG", SEGMENTS["AIG"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "SQR_S25_LOCATION_RESOURCE": (
        "sequence",
        (
            ["AIL", SEGMENTS["AIL"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "SQR_S25_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PV1", SEGMENTS["PV1"], (0, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
            ["DG1", SEGMENTS["DG1"], (0, 1), "SEG"],
        ),
    ),
    "SQR_S25_PERSONNEL_RESOURCE": (
        "sequence",
        (
            ["AIP", SEGMENTS["AIP"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "SQR_S25_RESOURCES": (
        "sequence",
        (
            ["RGS", SEGMENTS["RGS"], (1, 1), "SEG"],
            ["SQR_S25_SERVICE", None, (0, -1), "GRP"],
            ["SQR_S25_GENERAL_RESOURCE", None, (0, -1), "GRP"],
            ["SQR_S25_PERSONNEL_RESOURCE", None, (0, -1), "GRP"],
            ["SQR_S25_LOCATION_RESOURCE", None, (0, -1), "GRP"],
        ),
    ),
    "SQR_S25_SCHEDULE": (
        "sequence",
        (
            ["SCH", SEGMENTS["SCH"], (1, 1), "SEG"],
            ["TQ1", SEGMENTS["TQ1"], (0, -1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["SQR_S25_PATIENT", None, (0, 1), "GRP"],
            ["SQR_S25_RESOURCES", None, (1, -1), "GRP"],
        ),
    ),
    "SQR_S25_SERVICE": (
        "sequence",
        (
            ["AIS", SEGMENTS["AIS"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "SRM_S01_GENERAL_RESOURCE": (
        "sequence",
        (
            ["AIG", SEGMENTS["AIG"], (1, 1), "SEG"],
            ["APR", SEGMENTS["APR"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "SRM_S01_LOCATION_RESOURCE": (
        "sequence",
        (
            ["AIL", SEGMENTS["AIL"], (1, 1), "SEG"],
            ["APR", SEGMENTS["APR"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "SRM_S01_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PV1", SEGMENTS["PV1"], (0, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
            ["OBX", SEGMENTS["OBX"], (0, -1), "SEG"],
            ["DG1", SEGMENTS["DG1"], (0, -1), "SEG"],
        ),
    ),
    "SRM_S01_PERSONNEL_RESOURCE": (
        "sequence",
        (
            ["AIP", SEGMENTS["AIP"], (1, 1), "SEG"],
            ["APR", SEGMENTS["APR"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "SRM_S01_RESOURCES": (
        "sequence",
        (
            ["RGS", SEGMENTS["RGS"], (1, 1), "SEG"],
            ["SRM_S01_SERVICE", None, (0, -1), "GRP"],
            ["SRM_S01_GENERAL_RESOURCE", None, (0, -1), "GRP"],
            ["SRM_S01_LOCATION_RESOURCE", None, (0, -1), "GRP"],
            ["SRM_S01_PERSONNEL_RESOURCE", None, (0, -1), "GRP"],
        ),
    ),
    "SRM_S01_SERVICE": (
        "sequence",
        (
            ["AIS", SEGMENTS["AIS"], (1, 1), "SEG"],
            ["APR", SEGMENTS["APR"], (0, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "SRR_S01_GENERAL_RESOURCE": (
        "sequence",
        (
            ["AIG", SEGMENTS["AIG"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "SRR_S01_LOCATION_RESOURCE": (
        "sequence",
        (
            ["AIL", SEGMENTS["AIL"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "SRR_S01_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["PV1", SEGMENTS["PV1"], (0, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
            ["DG1", SEGMENTS["DG1"], (0, -1), "SEG"],
        ),
    ),
    "SRR_S01_PERSONNEL_RESOURCE": (
        "sequence",
        (
            ["AIP", SEGMENTS["AIP"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "SRR_S01_RESOURCES": (
        "sequence",
        (
            ["RGS", SEGMENTS["RGS"], (1, 1), "SEG"],
            ["SRR_S01_SERVICE", None, (0, -1), "GRP"],
            ["SRR_S01_GENERAL_RESOURCE", None, (0, -1), "GRP"],
            ["SRR_S01_LOCATION_RESOURCE", None, (0, -1), "GRP"],
            ["SRR_S01_PERSONNEL_RESOURCE", None, (0, -1), "GRP"],
        ),
    ),
    "SRR_S01_SCHEDULE": (
        "sequence",
        (
            ["SCH", SEGMENTS["SCH"], (1, 1), "SEG"],
            ["TQ1", SEGMENTS["TQ1"], (0, -1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
            ["SRR_S01_PATIENT", None, (0, -1), "GRP"],
            ["SRR_S01_RESOURCES", None, (1, -1), "GRP"],
        ),
    ),
    "SRR_S01_SERVICE": (
        "sequence",
        (
            ["AIS", SEGMENTS["AIS"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "SSR_U04_SPECIMEN_CONTAINER": (
        "sequence",
        (
            ["SAC", SEGMENTS["SAC"], (1, 1), "SEG"],
            ["SPM", SEGMENTS["SPM"], (0, -1), "SEG"],
        ),
    ),
    "SSU_U03_SPECIMEN": (
        "sequence",
        (
            ["SPM", SEGMENTS["SPM"], (1, 1), "SEG"],
            ["OBX", SEGMENTS["OBX"], (0, -1), "SEG"],
        ),
    ),
    "SSU_U03_SPECIMEN_CONTAINER": (
        "sequence",
        (
            ["SAC", SEGMENTS["SAC"], (1, 1), "SEG"],
            ["OBX", SEGMENTS["OBX"], (0, -1), "SEG"],
            ["SSU_U03_SPECIMEN", None, (0, -1), "GRP"],
        ),
    ),
    "SUR_P09_FACILITY": (
        "sequence",
        (
            ["FAC", SEGMENTS["FAC"], (1, 1), "SEG"],
            ["SUR_P09_PRODUCT", None, (1, -1), "GRP"],
            ["PSH", SEGMENTS["PSH"], (1, 1), "SEG"],
            ["SUR_P09_FACILITY_DETAIL", None, (1, -1), "GRP"],
        ),
    ),
    "SUR_P09_FACILITY_DETAIL": (
        "sequence",
        (
            ["FAC", SEGMENTS["FAC"], (1, 1), "SEG"],
            ["PDC", SEGMENTS["PDC"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (1, 1), "SEG"],
        ),
    ),
    "SUR_P09_PRODUCT": (
        "sequence",
        (
            ["PSH", SEGMENTS["PSH"], (1, 1), "SEG"],
            ["PDC", SEGMENTS["PDC"], (1, 1), "SEG"],
        ),
    ),
    "TCU_U10_TEST_CONFIGURATION": (
        "sequence",
        (
            ["SPM", SEGMENTS["SPM"], (0, 1), "SEG"],
            ["TCC", SEGMENTS["TCC"], (1, -1), "SEG"],
        ),
    ),
    "VXR_V03_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, 1), "SEG"],
        ),
    ),
    "VXR_V03_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "VXR_V03_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["VXR_V03_TIMING", None, (0, -1), "GRP"],
            ["RXA", SEGMENTS["RXA"], (1, 1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (0, 1), "SEG"],
            ["VXR_V03_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "VXR_V03_PATIENT_VISIT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "VXR_V03_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "VXU_V04_INSURANCE": (
        "sequence",
        (
            ["IN1", SEGMENTS["IN1"], (1, 1), "SEG"],
            ["IN2", SEGMENTS["IN2"], (0, 1), "SEG"],
            ["IN3", SEGMENTS["IN3"], (0, 1), "SEG"],
        ),
    ),
    "VXU_V04_OBSERVATION": (
        "sequence",
        (
            ["OBX", SEGMENTS["OBX"], (1, 1), "SEG"],
            ["NTE", SEGMENTS["NTE"], (0, -1), "SEG"],
        ),
    ),
    "VXU_V04_ORDER": (
        "sequence",
        (
            ["ORC", SEGMENTS["ORC"], (1, 1), "SEG"],
            ["VXU_V04_TIMING", None, (0, -1), "GRP"],
            ["RXA", SEGMENTS["RXA"], (1, 1), "SEG"],
            ["RXR", SEGMENTS["RXR"], (0, 1), "SEG"],
            ["VXU_V04_OBSERVATION", None, (0, -1), "GRP"],
        ),
    ),
    "VXU_V04_PATIENT": (
        "sequence",
        (
            ["PV1", SEGMENTS["PV1"], (1, 1), "SEG"],
            ["PV2", SEGMENTS["PV2"], (0, 1), "SEG"],
        ),
    ),
    "VXU_V04_TIMING": (
        "sequence",
        (
            ["TQ1", SEGMENTS["TQ1"], (1, 1), "SEG"],
            ["TQ2", SEGMENTS["TQ2"], (0, -1), "SEG"],
        ),
    ),
    "VXX_V02_PATIENT": (
        "sequence",
        (
            ["PID", SEGMENTS["PID"], (1, 1), "SEG"],
            ["NK1", SEGMENTS["NK1"], (0, -1), "SEG"],
        ),
    ),
}
for k, v in iteritems(GROUPS):
    for item in v[1]:
        if item[3] == "GRP":
            item[1] = GROUPS[item[0]]
