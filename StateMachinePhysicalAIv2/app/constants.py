from player import Player
from tile import Tile
from deed import Deed
from earningSpace import EarningSpace
from property import Property
from railroad import Railroad
from utility import Utility
from goToJail import GoToJail
from jail import Jail
from deck import Deck
from typing import List

class const():
    GO_MONEY = 200
    JAIL_FEE = 50
class property_stuff():
    Go = EarningSpace("Fight On!", 200)
    IncomeTax = EarningSpace("Tuition", -200)
    LuxuryTax = EarningSpace("Makers Dues", -100)
    FreeParking = EarningSpace("Coliseum", 0)
    GotoJail = GoToJail("Bruins")
    VisitJail = Jail("UCLA")
    MediterraneanAvenue = Property("KAP", 60, "brown", 2, 50, 10, 30, 90, 160, 250)
    BalticAvenue = Property("SAL", 60, "brown", 4, 50, 20, 60, 180, 320, 450)
    ReadingRR = Railroad("EVK Dining Hall", 200, "railroad", 25)
    OrientalAvenue = Property("RRB", 100, "lightblue", 6, 50, 30, 90, 270, 400, 550)
    VermontAvenue = Property("SLH", 100, "lightblue", 6, 50, 30, 90, 270, 400, 550)
    ConnecticutAvenue = Property("THH", 120, "lightblue", 8, 40, 100, 300, 450, 600, 550)
    CharlesPlace = Property("VHE", 140, "pink", 10, 100, 50, 150, 450, 625, 750)
    ElectricCompany = Utility("Tommy Trojan", 150, "utility", None)
    StatesAvenue = Property("SGM", 140, "pink", 10, 100, 50, 150, 450, 625, 750)
    VirginiaAvenue = Property("WPH", 160, "pink", 12, 100, 60, 180, 500, 700, 900)
    PennsylvaniaRR = Railroad("Parkside Dining Hall", 200, "railroad", 25)
    JamesPlace = Property("OHE", 180, "orange", 14, 100, 70, 200, 550, 750, 950)
    TennesseeAvenue = Property("GFS", 180, "orange", 14, 100, 70, 200, 550, 750, 950)
    NewYorkAvenue = Property("DMC", 200, "orange", 16, 100, 80, 220, 600, 800, 1000)
    KentuckyAvenue = Property("ZHS", 220, "red", 18, 150, 90, 250, 700, 875, 1050)
    IndianaAvenue = Property("KDC", 220, "red", 18, 150, 90, 250, 700, 875, 1050)
    IllinoisAvenue = Property("RTH", 240, "red", 20, 150, 100, 300, 750, 925, 1100)
    BoRR = Railroad("Village Dining Hall", 200, "railroad", 25)
    AtlanticAvenue = Property("SKS", 260, "yellow", 22, 150, 110, 330, 800, 975, 1150)
    VentnorAvenue = Property("JFF", 260, "yellow", 22, 150, 110, 330, 800, 975, 1150)
    WaterWorks = Utility("Traveler", 150, "utility", None)
    MarvinGardens = Property("MHP", 280, "yellow", 24, 150, 120, 360, 850, 1025, 1200)
    PacificAvenue = Property("IYA", 300, "green", 26, 200, 130, 390, 900, 1100, 1275)
    NorthCarolinaAvenue = Property("MCB", 300, "green", 26, 200, 130, 390, 900, 1100, 1275)
    PennsylvaniaAvenue = Property("SCA", 320, "green", 28, 200, 150, 450, 1000, 1200, 1400)
    ShortLine = Railroad("TCC", 200, "railroad", 25)
    ParkPlace = Property("EEB 132", 350, "darkblue", 35, 175, 500, 1100, 700, 1300, 1500)
    Boardwalk = Property("Robert", 400, "darkblue", 50, 150, 200, 600, 1400, 1700, 2000)
    CommunityChest = Deck("Isaac", True)
    Chance = Deck("Pooja", True)

    Tiles = [Go, MediterraneanAvenue, CommunityChest, BalticAvenue, IncomeTax, ReadingRR, OrientalAvenue, Chance, VermontAvenue, ConnecticutAvenue, VisitJail,
                        CharlesPlace, ElectricCompany, StatesAvenue, VirginiaAvenue, PennsylvaniaRR, JamesPlace, CommunityChest, TennesseeAvenue, NewYorkAvenue, FreeParking,
                        KentuckyAvenue, Chance, IndianaAvenue, IllinoisAvenue, BoRR, AtlanticAvenue, VentnorAvenue, WaterWorks, MarvinGardens, GotoJail,
                        PacificAvenue, NorthCarolinaAvenue, CommunityChest, PennsylvaniaAvenue, ShortLine, Chance, ParkPlace, LuxuryTax, Boardwalk]

    Deeds = [MediterraneanAvenue, BalticAvenue, OrientalAvenue, VermontAvenue, ConnecticutAvenue, CharlesPlace, StatesAvenue, VirginiaAvenue, JamesPlace, TennesseeAvenue,
            NewYorkAvenue, KentuckyAvenue, IndianaAvenue, IllinoisAvenue, AtlanticAvenue, VentnorAvenue, MarvinGardens, PacificAvenue,
            NorthCarolinaAvenue, PennsylvaniaAvenue, ParkPlace, Boardwalk, ReadingRR, PennsylvaniaRR, BoRR, ShortLine, ElectricCompany, WaterWorks]

    SetToDeedMap = {"railroad": [ReadingRR, PennsylvaniaRR, BoRR, ShortLine],
                    "utility": [ElectricCompany, WaterWorks],
                    "brown": [MediterraneanAvenue, BalticAvenue],
                    "lightblue": [OrientalAvenue, VermontAvenue, ConnecticutAvenue],
                    "pink": [CharlesPlace, StatesAvenue, VirginiaAvenue],
                    "orange": [JamesPlace, TennesseeAvenue, NewYorkAvenue],
                    "red": [KentuckyAvenue, IndianaAvenue, IllinoisAvenue],
                    "yellow": [AtlanticAvenue, VentnorAvenue, MarvinGardens],
                    "green": [PacificAvenue, NorthCarolinaAvenue, PennsylvaniaAvenue],
                    "darkblue": [ParkPlace, Boardwalk]} 
