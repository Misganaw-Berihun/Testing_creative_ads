from pydantic import BaseModel
from typing import List, Optional

class RedirectURL(BaseModel):
    redirect_url: str

class ThirdPartyEngagement(BaseModel):
    engagement_url: str

class TTDMetadata(BaseModel):
    dsp: str
    ttd_imp_aud_user_ttl_min: Optional[str]
    ttd_adformat: Optional[str]
    ttd_adgroupid: Optional[str]
    ttd_advertiserid: Optional[str]
    ttd_all_categories: Optional[str]
    ttd_base_bid_override_metadata: Optional[str]
    ttd_campaignid: Optional[str]
    ttd_category: Optional[str]
    ttd_city: Optional[str]
    ttd_country: Optional[str]
    ttd_creativeid: Optional[str]
    ttd_dealid: Optional[str]
    ttd_deviceosfamily: Optional[str]
    ttd_devicetype: Optional[str]
    ttd_devicemake: Optional[str]
    ttd_devicemodel: Optional[str]
    ttd_gdpr_applies: Optional[str]
    ttd_gdpr_consent_strinG: Optional[str]
    ttd_impressionid: Optional[str]
    ttd_language: Optional[str]
    ttd_metro: Optional[str]
    ttd_partnerid: Optional[str]
    ttd_privatecontractid: Optional[str]
    ttd_publisherid: Optional[str]
    ttd_region: Optional[str]
    ttd_rendering_context: Optional[str]
    ttd_site: Optional[str]
    ttd_site_with_path: Optional[str]
    ttd_supplyvendor: Optional[str]
    ttd_tdid: Optional[str]
    ttd_trustesid: Optional[str]
    ttd_unix_timestamp: Optional[str]
    ttd_zipcode: Optional[str]

class GameResponse(BaseModel):
    game_key: str
    lorenzo_id: Optional[str]
    region: Optional[str]
    environment: Optional[str]
    service_level: Optional[str]
    width: Optional[int]
    height: Optional[int]
    redirect_urls: List[RedirectURL] = []
    third_party_engagement: List[ThirdPartyEngagement] = []
    ttd_metadata: Optional[TTDMetadata]

class Event(BaseModel):
    id: int
    action_type: str
    event_type: str

class AdUnitCreate(BaseModel):
    game_key: str
    lorenzo_id: Optional[str]
    region: Optional[str]
    environment: Optional[str]
    service_level: Optional[str]
    width: Optional[int]
    height: Optional[int]
    redirect_urls: List[str] 
    dsp: Optional[str]
    third_party_engagement: List[str] = []
    ttd_imp_aud_user_ttl_min: Optional[str]
    ttd_adformat: Optional[str]
    ttd_adgroupid: Optional[str]
    ttd_advertiserid: Optional[str]
    ttd_all_categories: Optional[str]
    ttd_base_bid_override_metadata: Optional[str]
    ttd_campaignid: Optional[str]
    ttd_category: Optional[str]
    ttd_city: Optional[str]
    ttd_country: Optional[str]
    ttd_creativeid: Optional[str]
    ttd_dealid: Optional[str]
    ttd_deviceosfamily: Optional[str]
    ttd_devicetype: Optional[str]
    ttd_devicemake: Optional[str]
    ttd_devicemodel: Optional[str]
    ttd_gdpr_applies: Optional[str]
    ttd_gdpr_consent_strinG: Optional[str]
    ttd_impressionid: Optional[str]
    ttd_language: Optional[str]
    ttd_metro: Optional[str]
    ttd_partnerid: Optional[str]
    ttd_privatecontractid: Optional[str]
    ttd_publisherid: Optional[str]
    ttd_region: Optional[str]
    ttd_rendering_context: Optional[str]
    ttd_site: Optional[str]
    ttd_site_with_path: Optional[str]
    ttd_supplyvendor: Optional[str]
    ttd_tdid: Optional[str]
    ttd_trustesid: Optional[str]
    ttd_unix_timestamp: Optional[str]
    ttd_zipcode: Optional[str]