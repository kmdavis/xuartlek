---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Divine Warden Of Pharasma"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Divine Warden Of Pharasma"
level: 6
source: "Monster Core 2"
aon_id: "creature-4338"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4338"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Divine Warden Of Pharasma"
level: "Creature 6"
size: "Large"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: "Uncommon"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +15"
abilityMods: [5, -2, 4, -5, 0, -5]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +17; __Ref__: +11; __Will__: +14"
hp: 95
health:
  - name: "HP"
    desc: "95; __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, mental, nonlethal attacks, paralyzed, poison, sickened, spirit, unconscious, vitality, void"
abilities_mid:
  - name: "Divine Destruction"
    desc: "(divine, spirit) When the divine warden is reduced to 0 HP, it erupts with divine energy in a 30-foot emanation, dealing 7d6 spirit damage per level. Each creature in the area must attempt a DC 21 Will save with the following outcomes."
  - name: "Critical Success"
    desc: "The creature takes half damage."
  - name: "Success"
    desc: "The creature takes full damage."
  - name: "Failure"
    desc: "The creature takes full damage and becomes temporarily cursed by the patron deity. The creature becomes enfeebled 1 and stupefied 1 for 1 day; this is a curse effect that uses the Will save DC as the counteract DC."
  - name: "Critical Failure"
    desc: "As failure, except the creature becomes enfeebled 2 and stupefied 2."
  - name: "Faith Bound"
    desc: "(divine) A divine warden can't attack a creature that openly wears or displays the religious symbol of the divine warden's patron deity unless that creature uses a hostile action against the divine warden first. If the divine warden is intelligent, it can also attack a creature it believes isn't faithful to its deity or who wears the religious symbol as a ruse (typically after succeeding at a Perception check to Sense Motive)."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +16 (Agile, magical, versatile S) __Damage__ 2d4+7 piercing"
abilities_bot:
  - name: "Faithful Weapon"
    desc: "A divine warden always wields its patron deity's favored weapon. If the weapon is a ranged weapon, the divine warden automatically generates new ammunition with each attack. For a divine warden of 4th level or higher, the deity's favored weapon gains the effects of a _striking_ rune while the divine warden wields it. The Divine Warden of Pharasma wields a dagger with a _striking_ rune."
  - name: "Instrument of Faith"
    desc: "The divine warden is a beacon for its deity's faith. A cleric of Pharasma can channel a _heal_ spell through the divine warden they can see within 60 feet. The cleric determines any targets or area for the spell as if they were standing in the divine warden's space."
  - name: "Mask of Fate"
    desc: "⬺ (Divine, misfortune) The divine warden of Pharasma peers at a single creature within 60 feet through the eyes of its mask to alter its destiny. The target must attempt a DC 21 Will save."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "The target takes a –1 status penalty to the next saving throw it attempts within the next minute against a divine effect from a divine warden of Pharasma or worshipper of Pharasma."
  - name: "Failure"
    desc: "For the next saving throw the target attempts within the next minute against a divine effect from a divine warden of Pharasma or worshipper of Pharasma, it rolls twice and takes the worse result."
  - name: "Critical Failure"
    desc: "As failure, but the misfortune effect applies to all applicable saving throws."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 21, attack +13 - __Cantrips (3rd)__ Divine Lance __Divine Domain Spells,__ DC 21 1 Focus Point - __3rd__ Death's Call, Healer's Blessing"
sourcebook: "_Monster Core 2_, page 115."
```

```encounter-table
name: Divine Warden Of Pharasma
creatures:
  - 1: Divine Warden Of Pharasma
```
