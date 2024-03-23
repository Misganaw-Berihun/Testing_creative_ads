from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Game(Base):
    __tablename__ = 'game'
    game_key = Column(String(100), primary_key=True)
    lorenzo_id = Column(String(100))
    region = Column(String(50))
    environment = Column(String(50))
    service_level = Column(String(50))
    width = Column(Integer)
    height = Column(Integer)
    redirect_urls = relationship("RedirectURLs", back_populates="game")
    third_party_engagement = relationship("ThirdPartyEngagement", back_populates="game")
    ttd_metadata = relationship("TTDMetadata", uselist=False, back_populates="game")

class RedirectURLs(Base):
    __tablename__ = 'redirect_urls'
    id = Column(Integer, primary_key=True)
    game_key = Column(String(100), ForeignKey('game.game_key'))
    redirect_url = Column(String(255))
    game = relationship("Game", back_populates="redirect_urls")

class ThirdPartyEngagement(Base):
    __tablename__ = 'third_party_engagement'
    id = Column(Integer, primary_key=True)
    game_key = Column(String(100), ForeignKey('game.game_key'))
    engagement_url = Column(Text)
    game = relationship("Game", back_populates="third_party_engagement")

class TTDMetadata(Base):
    __tablename__ = 'ttd_metadata'
    game_key = Column(String(100), ForeignKey('game.game_key'), primary_key=True)
    dsp = Column(String(50))
    ttd_imp_aud_user_ttl_min = Column(String(255))
    ttd_adformat = Column(String(255))
    ttd_adgroupid = Column(String(255))
    ttd_advertiserid = Column(String(255))
    ttd_all_categories = Column(String(255))
    ttd_base_bid_override_metadata = Column(String(255))
    ttd_campaignid = Column(String(255))
    ttd_category = Column(String(255))
    ttd_city = Column(String(255))
    ttd_country = Column(String(255))
    ttd_creativeid = Column(String(255))
    ttd_dealid = Column(String(255))
    ttd_deviceosfamily = Column(String(255))
    ttd_devicetype = Column(String(255))
    ttd_devicemake = Column(String(255))
    ttd_devicemodel = Column(String(255))
    ttd_gdpr_applies = Column(String(255))
    ttd_gdpr_consent_string = Column(String(255))
    ttd_impressionid = Column(String(255))
    ttd_language = Column(String(255))
    ttd_metro = Column(String(255))
    ttd_partnerid = Column(String(255))
    ttd_privatecontractid = Column(String(255))
    ttd_publisherid = Column(String(255))
    ttd_region = Column(String(255))
    ttd_rendering_context = Column(String(255))
    ttd_site = Column(String(255))
    ttd_site_with_path = Column(String(255))
    ttd_supplyvendor = Column(String(255))
    ttd_tdid = Column(String(255))
    ttd_trustesid = Column(String(255))
    ttd_unix_timestamp = Column(String(255))
    ttd_zipcode = Column(String(255))
    game = relationship("Game", back_populates="ttd_metadata")

class Event(Base):
    __tablename__ = 'event_table'
    id = Column(Integer, primary_key=True)
    action_type = Column(String)
    event_type = Column(String)
