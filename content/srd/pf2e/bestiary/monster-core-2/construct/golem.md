---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Golem"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/large
statblock: inline
name: "Golem"
level: 8
source: "Monster Core 2"
aon_id: "creature-4417"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4417"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Golem"
level: "Creature 8"
size: "Large"
trait_01: "Construct"
trait_02: "Earth"
trait_03: "Holy"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16"
languages: "Common; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "Athletics +20, Religion +18"
abilityMods: [6, 2, 5, 1, 4, 0]
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +19; __Ref__: +12; __Will__: +16"
hp: 170
health:
  - name: "HP"
    desc: "170; __Immunities__ acid, bleed, death effects, disease, doomed, drained, fatigued, healing, nonlethal attacks, paralyzed, poison, sickened, sleep, spirit, unconscious, vitality, void"
abilities_mid:
  - name: "Day of Rest"
    desc: "A golem needs 1 day of rest per week or it becomes uncontrollable. An uncontrollable golem is unable to cast spells, and it takes a –2 circumstance penalty to checks made using Wisdom, including Will saves. While uncontrollable, the golem loses its immunity to sleep. The golem is uncontrollable until it takes a day of rest."
  - name: "Faithful"
    desc: "A golem faithfully serves its creator as long as it's not in an uncontrollable state (see above). While the golem is faithful, it follows the commands of its creator, even to its own detriment. While the golem remains faithful to its creator, the golem can't be confused or controlled by any creature other than its creator."
  - name: "Hefty Helper"
    desc: "The golem can carry 13 Bulk before becoming encumbered and can carry a maximum Bulk of 18."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +20 (reach 10 feet) __Damage__ 2d10+8 bludgeoning plus consecrated fists"
abilities_bot:
  - name: "Consecrated Fists"
    desc: "(Divine) After the golem casts a holy spell, their Strikes deal an additional 1d8 spirit damage and gain the divine and holy traits. These benefits last until the end of the golem's next turn."
  - name: "Rampage"
    desc: "⬺"
  - name: "Requirements"
    desc: "The golem is uncontrollable"
  - name: "Effect"
    desc: "The golem makes a melee Strike against every creature in its reach, whether that creature is an ally or not. The attacks count toward its multiple attack penalty normally, but the penalty does not increase until after all the Strikes are complete. Temple Guardians Golems have been used to guard and assist at temples across the Inner Sea region, though they're said to have originated in northern Garund. Only followers of holy deities can create golems, most of which are given life by priests of Desna or Shelyn, or sometimes Casandalee."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 24, attack +16 - __Cantrips (4th)__ Divine Lance, Stabilize - __2nd__ Heal (×4) - __3rd__ Calm (×2), Holy Light (at will) - __4th__ Dispel Magic, Divine Wrath (×2)"
sourcebook: "_Monster Core 2_, page 169."
```

```encounter-table
name: Golem
creatures:
  - 1: Golem
```
