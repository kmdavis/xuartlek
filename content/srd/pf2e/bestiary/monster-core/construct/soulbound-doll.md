---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Soulbound Doll"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/soulbound
  - pf2e/creature/trait/tiny
statblock: inline
name: "Soulbound Doll"
level: 2
source: "Monster Core"
aon_id: "creature-3204"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3204"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Soulbound Doll"
level: "Creature 2"
size: "Tiny"
trait_01: "Construct"
trait_02: "Soulbound"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
languages: "Common; one spoken by its creator (typically Common)"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Occultism +4, Stealth +8"
abilityMods: [-2, 4, 3, 0, 2, 0]
abilities_top:
  - name: "Personality Fragments"
    desc: "A soulbound doll shares fragments of its donor soul's personality, though none of that creature's memories. This causes a soulbound doll to match a strong personality trait of the donor soul (see sidebar). Because of its soul sliver, a soulbound doll is not immune to spirit as most constructs are."
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +7; __Ref__: +10; __Will__: +6"
hp: 23
health:
  - name: "HP"
    desc: "23; __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, nonlethal attacks, paralyzed, poison, sickened, unconscious, vitality, void; __Resistances__ bludgeoning 3, piercing 5, slashing 3"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +10 (Agile, Finesse, Magical, reach 0 feet) __Damage__ 1d6+2 bludgeoning"
abilities_bot:
  - name: "Brave"
    desc: ": _enlarge_"
  - name: "Calm"
    desc: ": _calm_"
  - name: "Careful"
    desc: ": _augury_"
  - name: "Cruel"
    desc: ": _harm_"
  - name: "Gentle"
    desc: ": _peaceful rest_"
  - name: "Impish"
    desc: ": _disguise magic_"
  - name: "Jolly"
    desc: ": _laughing fit_"
  - name: "Kind"
    desc: ": _heal_"
  - name: "Rash"
    desc: ": _breathe fire_"
  - name: "Sassy"
    desc: ": _dispel magic_"
  - name: "Timid"
    desc: ": _invisibility_"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 18, attack +10 - __Cantrips (1st)__ Light, Prestidigitation, Telekinetic Hand - __2nd__ one spell based on donor soul's personality trait (see sidebar) - __3rd__ Levitate Soulbound Personalities A soulbound doll's additional 2nd-rank innate spell depends on a strong personality trait it had in life, as listed below."
sourcebook: "_Monster Core_, page 318."
```

```encounter-table
name: Soulbound Doll
creatures:
  - 1: Soulbound Doll
```
