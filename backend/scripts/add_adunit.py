import os, sys
from sqlalchemy.orm import sessionmaker

rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)


from db.tables import Game, RedirectURLs, ThirdPartyEngagement, TTDMetadata, Base

def add_ad_unit(session, ad_unit):
    game = Game(
        game_key=ad_unit['game_key'],
        lorenzo_id=ad_unit.get('lorenzo_id', None),
        region=ad_unit['region'],
        environment=ad_unit['environment'],
        service_level=ad_unit['service_level'],
        width=ad_unit['width'],
        height=ad_unit['height']
    )
    session.add(game)
    
    for redirect_url in ad_unit['redirect_urls']:
        redirect = RedirectURLs(game_key=ad_unit['game_key'], redirect_url=redirect_url)
        session.add(redirect)
    
    for engagement_url in ad_unit['third_party_engagement']:
        engagement = ThirdPartyEngagement(game_key=ad_unit['game_key'], engagement_url=engagement_url)
        session.add(engagement)
    
    ttd_metadata = TTDMetadata(game_key=ad_unit['game_key'], dsp=ad_unit['dsp'],
                                ttd_imp_aud_user_ttl_min=ad_unit['ttd_imp_aud_user_ttl_min'],
                                ttd_adformat=ad_unit['ttd_adformat'], ttd_adgroupid=ad_unit['ttd_adgroupid'],
                                ttd_advertiserid=ad_unit['ttd_advertiserid'],
                                ttd_all_categories=ad_unit['ttd_all_categories'],
                                ttd_base_bid_override_metadata=ad_unit['ttd_base_bid_override_metadata'],
                                ttd_campaignid=ad_unit['ttd_campaignid'], ttd_category=ad_unit['ttd_category'],
                                ttd_city=ad_unit['ttd_city'], ttd_country=ad_unit['ttd_country'],
                                ttd_creativeid=ad_unit['ttd_creativeid'], ttd_dealid=ad_unit['ttd_dealid'],
                                ttd_deviceosfamily=ad_unit['ttd_deviceosfamily'],
                                ttd_devicetype=ad_unit['ttd_devicetype'], ttd_devicemake=ad_unit['ttd_devicemake'],
                                ttd_devicemodel=ad_unit['ttd_devicemodel'],
                                ttd_gdpr_applies=ad_unit['ttd_gdpr_applies'],
                                ttd_gdpr_consent_strinG=ad_unit['ttd_gdpr_consent_strinG'],
                                ttd_impressionid=ad_unit['ttd_impressionid'], ttd_language=ad_unit['ttd_language'],
                                ttd_metro=ad_unit['ttd_metro'], ttd_partnerid=ad_unit['ttd_partnerid'],
                                ttd_privatecontractid=ad_unit['ttd_privatecontractid'],
                                ttd_publisherid=ad_unit['ttd_publisherid'], ttd_region=ad_unit['ttd_region'],
                                ttd_rendering_context=ad_unit['ttd_rendering_context'],
                                ttd_site=ad_unit['ttd_site'], ttd_site_with_path=ad_unit['ttd_site_with_path'],
                                ttd_supplyvendor=ad_unit['ttd_supplyvendor'], ttd_tdid=ad_unit['ttd_tdid'],
                                ttd_trustesid=ad_unit['ttd_trustesid'], ttd_unix_timestamp=ad_unit['ttd_unix_timestamp'],
                                ttd_zipcode=ad_unit['ttd_zipcode'])
    session.add(ttd_metadata)
