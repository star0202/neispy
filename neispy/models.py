from datetime import datetime


class School:
    def __init__(self, data: dict):
        self.ATPT_OFCDC_SC_CODE: str = data["ATPT_OFCDC_SC_CODE"]  # 시도교육청코드
        self.ATPT_OFCDC_SC_NM: str = data["ATPT_OFCDC_SC_NM"]  # 시도교육청명
        self.SD_SCHUL_CODE: int = int(data["SD_SCHUL_CODE"])  # 표준학교코드
        self.SCHUL_NM: str = data["SCHUL_NM"]  # 학교명
        self.ENG_SCHUL_NM: str = data["ENG_SCHUL_NM"]  # 영문학교명
        self.SCHUL_KND_SC_NM: str = data["SCHUL_KND_SC_NM"]  # 학교종류명
        self.LCTN_SC_NM: str = data["LCTN_SC_NM"]  # 소재지명
        self.JU_ORG_NM: str = data["JU_ORG_NM"]  # 관할조직명
        self.FOND_SC_NM: str = data["FOND_SC_NM"]  # 설립명
        self.ORG_RDNZC: int = int(data["ORG_RDNZC"])  # 도로명우편번호
        self.ORG_RDNMA: str = data["ORG_RDNMA"]  # 도로명주소
        self.ORG_RDNDA: str = data["ORG_RDNDA"]  # 도로명상세주소
        self.ORG_TELNO: str = data["ORG_TELNO"]  # 전화번호
        self.HMPG_ADRES: str = data["HMPG_ADRES"]  # 홈페이지주소
        self.COEDU_SC_NM: str = data["COEDU_SC_NM"]  # 남녀공학구분명
        self.ORG_FAXNO: str = data["ORG_FAXNO"]  # 팩스번호
        self.HS_SC_NM: str | None = data["HS_SC_NM"]  # 고등학교구분명
        self.INDST_SPECL_CCCCL_EXST_YN: bool  # 산업체특별학급존재여부
        if data["INDST_SPECL_CCCCL_EXST_YN"] == "Y":
            self.INDST_SPECL_CCCCL_EXST_YN = True
        elif data["INDST_SPECL_CCCCL_EXST_YN"] == "N":
            self.INDST_SPECL_CCCCL_EXST_YN = False
        self.HS_GNRL_BUSNS_SC_NM: str | None  # 고등학교일반실업구분명
        if data["HS_GNRL_BUSNS_SC_NM"] == "해당없음":
            self.HS_GNRL_BUSNS_SC_NM = None
        else:
            self.HS_GNRL_BUSNS_SC_NM = data["HS_GNRL_BUSNS_SC_NM"]
        self.SPCLY_PURPS_HS_ORD_NM: str | None = data["SPCLY_PURPS_HS_ORD_NM"]  # 특수목적고등학교계열명
        self.ENE_BFE_SEHF_SC_NM: str = data["ENE_BFE_SEHF_SC_NM"]  # 입시전후기구분명
        self.DGHT_SC_NM: str = data["DGHT_SC_NM"]  # 주야구분명
        self.FOND_YMD: datetime = datetime.strptime(data["FOND_YMD"], "%Y%m%d")  # 설립일자
        self.FOAS_MEMRD: datetime = datetime.strptime(data["FOAS_MEMRD"], "%Y%m%d")  # 개교기념일
        self.LOAD_DTM: datetime = datetime.strptime(data["LOAD_DTM"], "%Y%m%d")  # 수정일

    def __str__(self):
        return f"{self.ATPT_OFCDC_SC_CODE} {self.SD_SCHUL_CODE} {self.SCHUL_NM}"
