from hero import Hero
from elf import Elf
from wizard import Wizard
from knight import Knight
from muse_elf import MuseElf
from dark_knight import DarkKnight
from dark_wizard import DarkWizard
from soul_master import SoulMaster
from blade_knight import BladeKnight

if __name__ == "__main__":
    hero = Hero("H", 4)
    print(hero.username)
    print(hero.level)
    print(str(hero))

    elf = Elf("E", 4)
    print(str(elf))
    print(elf.__class__.__bases__[0].__name__)
    print(elf.username)
    print(elf.level)

    wizard = Wizard("E", 4)
    print(str(wizard))
    print(wizard.__class__.__bases__[0].__name__)
    print(wizard.username)
    print(wizard.level)

    knight = Knight("E", 4)
    print(str(knight))
    print(knight.__class__.__bases__[0].__name__)
    print(knight.username)
    print(knight.level)

    muse_elf = MuseElf("E", 4)
    print(str(muse_elf))
    print(muse_elf.__class__.__bases__[0].__name__)
    print(muse_elf.username)
    print(muse_elf.level)

    dark_wizzard = DarkWizard("E", 4)
    print(str(dark_wizzard))
    print(dark_wizzard.__class__.__bases__[0].__name__)
    print(dark_wizzard.username)
    print(dark_wizzard.level)

    dark_knight = DarkKnight("E", 4)
    print(str(dark_knight))
    print(dark_knight.__class__.__bases__[0].__name__)
    print(dark_knight.username)
    print(dark_knight.level)

    soul_master = SoulMaster("E", 4)
    print(str(soul_master))
    print(soul_master.__class__.__bases__[0].__name__)
    print(soul_master.username)
    print(soul_master.level)

    bladeknight = BladeKnight("E", 4)
    bladeknight.username = "LOl"
    bladeknight.level = 155
    print(str(bladeknight))
    print(bladeknight.__class__.__bases__[0].__name__)
    print(bladeknight.username)
