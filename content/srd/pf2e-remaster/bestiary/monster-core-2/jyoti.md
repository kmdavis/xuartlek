---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Jyoti"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/vitality
  - pf2e/creature/trait/medium
  - pf2e/creature/trait/positive
statblock: inline
name: "Jyoti"
level: 9
source: "Monster Core 2"
aon_id: "creature-4452"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4452"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Jyoti"
level: "Creature 9"
size: "Medium"
trait_01: "Fire"
trait_02: "Humanoid"
trait_03: "Vitality"
trait_04: "Positive"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; darkvision"
languages: "Common, Jyoti"
skills:
  - name: "Skills"
    desc: "Acrobatics +20, Intimidation +18, Occultism +20, Society +18"
abilityMods: [3, 5, 4, 5, 6, 3]
abilities_top:
  - name: "Items"
    desc: "_+1 striking longspear_"
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +15; __Ref__: +18; __Will__: +21 +1 status to all saves vs. magic (+2 vs. divine magic)"
hp: 155
health:
  - name: "HP"
    desc: "155; __Immunities__ death effects, disease, poison; __Resistances__ fire 10, void 10"
abilities_mid:
  - name: "Vitality Energy Affinity"
    desc: "Vitality healing effects always heal the jyoti for the maximum amount. It doesn't gain the automatic Hit Points or temporary Hit Points from being on a plane with the vitality planar essence trait."
speed: "25 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _flaming ghost touch longspear_ +20 (Magical, reach 10 feet) __Damage__ 2d8+6 piercing plus 1d6 fire"
  - name: "Melee"
    desc: "⬻ beak +21 (Finesse) __Damage__ 2d12+6 piercing plus 1d6 fire"
  - name: "Melee"
    desc: "⬻ talon +21 (Agile, finesse) __Damage__ 2d8+6 slashing plus 1d6 fire"
abilities_bot:
  - name: "Breath of Burning Life"
    desc: "(Fire, occult, vitality) The jyoti breathes a blast of searing flame infused with vitality energy in a 40-foot cone that deals 8d6 fire damage plus 4d6 vitality damage to creatures in the area (DC 28 basic Reflex save). The jyoti can't use Breath of Burning Life again for 1d4 rounds."
  - name: "Infuse Weapons"
    desc: "(Occult) Any weapon a jyoti wields becomes a _flaming ghost touch weapon_ while the jyoti holds it. Crystal Vaults Jyotis make ideal guardians for artifacts too dangerous to be left where those hungry for power might seize them. Only they know what items of myth and legend, long thought lost or destroyed, lie within their crystal vaults. They're unreliable guardians of religious artifacts, however, which usually disgust them."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 28, attack +20 - __Cantrips (5th)__ Light, Vitality Lash - __2nd__ Cleanse Affliction, Clear Mind, Sound Body - __3rd__ Heal (×3) - __4th__ Heal, Holy Light, Translocate - __5th__ Banishment, Breath of Life"
sourcebook: "_Monster Core 2_, page 203."
```

```encounter-table
name: Jyoti
creatures:
  - 1: Jyoti
```
