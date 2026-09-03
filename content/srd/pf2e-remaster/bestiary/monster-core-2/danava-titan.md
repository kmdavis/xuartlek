---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Danava Titan"
tags:
  - pf2e/creature/level/23
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/titan
  - pf2e/creature/trait/water
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Danava Titan"
level: 23
source: "Monster Core 2"
aon_id: "creature-4583"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4583"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Danava Titan"
level: "Creature 23"
size: "Gargantuan"
trait_01: "Humanoid"
trait_02: "Rare"
trait_03: "Titan"
trait_04: "Water"
modifier: 41
perception:
  - name: "Perception"
    desc: "Perception +41; darkvision, _truesight_, wavesense (imprecise) 100 feet"
languages: "Chthonian, Common, Empyrean, Thalassic; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +39, Arcana +43, Athletics +46, Crafting +43, Nature +41, Occultism +43, Religion +41, Society +43"
abilityMods: [11, 8, 10, 10, 8, 6]
abilities_top:
  - name: "Items"
    desc: "_+3 major striking greatclub_"
ac: 49
armorclass:
  - name: "AC"
    desc: "49; __Fort__: +41; __Ref__: +37; __Will__: +37 +4 status to all saves vs. mental or divine"
hp: 470
health:
  - name: "HP"
    desc: "470; __Immunities__ death effects, disease"
abilities_mid:
  - name: "Hadalic Presence"
    desc: "(divine, illusion, mental, water) Creatures that fail their Will save against the titan's impossible stature aura also experience the crushing depths and darkness of the ocean floor. Such creatures see as if in an area of _darkness_ (10th rank), and the titan can use their wavesense to detect such creatures as a precise sense, even if neither are in water. On a critical failure, the creature is also immobilized."
  - name: "Impossible Stature"
    desc: "(aura, divine, illusion, mental) 100 feet. Titans warp perception and distance around them to seem even larger and more imposing. A creature that enters or begins its turn within the emanation must succeed at a DC 46 Will save or its movement toward the titan is movement over difficult terrain (greater difficult terrain on a critical failure) for 1 round."
  - name: "Relentless"
    desc: "The titan is as ever-moving as ocean waves. They're permanently quickened 1, and the extra action can be used only to Stride, Strike, or Sustain a Spell, or as one of the actions necessary to cast _dispel magic_."
  - name: "Roiling Rebuke"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within 200 feet targets the titan with or includes the titan in the area of an attack, spell, or other effect"
  - name: "Effect"
    desc: "The titan makes a benthic wave Strike against the triggering creature. If the Strike hits, the titan disrupts the triggering action."
speed: "50 feet, fly 50 feet, swim 40 feet; water walk"
attacks:
  - name: "Melee"
    desc: "⬻ _greatclub_ +43 (Backswing, magical, reach 40 feet, shove) __Damage__ 4d10+20 bludgeoning plus 2d12 cold"
  - name: "Melee"
    desc: "⬻ foot +40 (Agile, reach 30 feet) __Damage__ 4d8+20 bludgeoning plus 2d12 cold"
  - name: "Ranged"
    desc: "⬻ benthic wave +40 (Brutal, magical, range 200 feet, water) __Damage__ 4d6+20 bludgeoning plus 2d12 cold"
abilities_bot:
  - name: "Trample"
    desc: "⬽ Huge or smaller, foot, DC 46"
  - name: "Wide Cleave"
    desc: "⬺ The titan makes a melee weapon Strike against each foe within their reach. This counts as three attacks for the titan's multiple attack penalty, but the penalty doesn't increase until all attacks have been made. Danava Pillars Some danavas, known as danava pillars, are custodians of a fundamental concept like life or knowledge—each, a crux of the universe. Destroying a danava pillar forcibly shreds their bonds and risks unraveling a portion of reality, with potentially disastrous effects."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 46, attack +38 - __9th__ Control Water (at will), Dispel Magic (at will), Eclipse Burst (×3), Heal (×3), Hydraulic Push (×3), Hydraulic Torrent (×3) - __10th__ Implosion - __Constant (10th)__ Truesight, Water Walk"
  - name: "Rituals"
    desc: "DC 46 - __5th__ Resurrect (doesn't require secondary casters) - __6th__ Binding Circle - __8th__ Control Weather"
sourcebook: "_Monster Core 2_, page 321."
```

```encounter-table
name: Danava Titan
creatures:
  - 1: Danava Titan
```
