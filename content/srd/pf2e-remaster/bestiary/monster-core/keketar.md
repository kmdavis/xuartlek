---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Keketar"
tags:
  - pf2e/creature/level/17
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/protean
  - pf2e/creature/trait/large
statblock: inline
name: "Keketar"
level: 17
source: "Monster Core"
aon_id: "creature-3146"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3146"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Keketar"
level: "Creature 17"
size: "Large"
trait_01: "Monitor"
trait_02: "Protean"
modifier: 30
perception:
  - name: "Perception"
    desc: "Perception +30; entropy sense (imprecise) 60 feet, darkvision"
languages: "Chthonian, Empyrean, Protean; telepathy 100 feet, _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +26, Athletics +33, Deception +32, Diplomacy +34, Intimidation +34, Religion +30, Stealth +30"
abilityMods: [8, 5, 7, 5, 7, 7]
abilities_top:
  - name: "Entropy Sense"
    desc: "(divine, prediction) A protean can anticipate the most likely presence of a creature through a supernatural insight into chaotic probabilities and chance. This grants them the ability to sense creatures within the listed range. _Veil of privacy_ prevents a creature from being detected via entropy sense automatically (without a counteract check)."
ac: 40
armorclass:
  - name: "AC"
    desc: "40; __Fort__: +30; __Ref__: +28; __Will__: +34 +1 status to all saves vs. magic"
hp: 260
health:
  - name: "HP"
    desc: "260 (fast healing 10); __Resistances__ precision 10, protean anatomy 25"
abilities_mid:
  - name: "Protean Anatomy"
    desc: "(divine) A protean's vital organs shift and change shape and position constantly. Immediately after the protean takes acid, electricity, or sonic damage, they gain the listed amount of resistance to that damage type. This lasts for 1 hour or until the next time the protean takes damage of one of the other types (in which case their resistance changes to match that type), whichever comes first. The protean is immune to polymorph effects unless they're a willing target. If blinded or deafened, the protean automatically recovers at the end of their next turn as new sensory organs grow to replace the compromised ones."
  - name: "Spatial Riptide"
    desc: "(aura, divine) 30 feet. A creature using a teleportation ability within the aura or arriving in it via teleportation must succeed at a DC 38 Fortitude save or wink out of existence for 1d4 rounds before completing the teleport. The creature can't act, sense anything, or be targeted. On a successful save, the creature completes the teleport normally but is stunned 1. Keketars are immune to this effect."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "40 feet, fly 50 feet, swim 40 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +33 (Magical, reach 10 feet) __Damage__ 3d12+16 piercing plus warpwave strike"
  - name: "Melee"
    desc: "⬻ claw +33 (Agile, Magical, reach 10 feet) __Damage__ 2d12+16 slashing plus warpwave strike"
  - name: "Melee"
    desc: "⬻ tail +33 (reach 15 feet) __Damage__ 2d12+16 bludgeoning plus Grab"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Divine, Polymorph) The keketar can take the appearance of any Huge or smaller creature. This doesn't change their Speed or their attack and damage bonuses with their Strikes but might change the damage type their Strikes deal."
  - name: "Constrict"
    desc: "⬻ 1d10+15 bludgeoning, DC 42"
  - name: "Reshape Reality"
    desc: "(Concentrate, Divine, Polymorph) When the keketar casts _mirage_, they infuse the illusion with quasi-real substance. Creatures that do not disbelieve the illusion treat structures and terrain created through the spell as though they were real, ascending illusory stairs, becoming trapped by illusory quicksand, and so on."
  - name: "Warpwave Strike"
    desc: "(Divine, Polymorph) A creature struck by a keketar's jaws or claw Strike must succeed at a DC 36 Fortitude save or be subject to a warpwave."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 42, attack +32 - __4th__ Confusion (at will), Translocate (at will), Unfettered Movement - __5th__ Creation (at will), Mirage (×2; see reshape reality), Translocate - __6th__ Teleport (at will; self only) - __7th__ Disintegrate, Dispel Magic (at will), Shatter (at will), Warp Mind (×3) - __8th__ Confusion, Cursed Metamorphosis - __9th__ Divine Wrath, Unfathomable Song - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core_, page 272."
```

```encounter-table
name: Keketar
creatures:
  - 1: Keketar
```
