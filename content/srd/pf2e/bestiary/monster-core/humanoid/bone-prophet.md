---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Bone Prophet"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/serpentfolk
  - pf2e/creature/trait/medium
statblock: inline
name: "Bone Prophet"
level: 8
source: "Monster Core"
aon_id: "creature-3185"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3185"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Bone Prophet"
level: "Creature 8"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Serpentfolk"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision, scent (imprecise) 30 feet"
languages: "Aklo, Common, Necril, Sakvroth; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Arcana +15, Deception +18, Intimidation +16, Occultism +17, Religion +19, Society +15, Stealth +13"
abilityMods: [3, 3, 2, 5, 5, 6]
abilities_top:
  - name: "Items"
    desc: "invisibility potion, religious symbol of Ydersius, _+1 striking staff_"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +14; __Ref__: +15; __Will__: +19 (+4 status vs. mental) +1 status to all saves vs. magic"
hp: 115
health:
  - name: "HP"
    desc: "115; __Resistances__ poison 10"
abilities_mid:
  - name: "Thin of Blood"
    desc: "Zyss serpentfolk recover slowly from injuries. When they take physical damage from a critical hit, they gain 2d4 persistent bleed damage. They take a –2 circumstance penalty to flat checks to recover from persistent damage and saving throws against afflictions."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _staff_ +18 (Magical, two-hand d8) __Damage__ 2d4+9 bludgeoning"
  - name: "Melee"
    desc: "⬻ fangs +17 (Finesse) __Damage__ 2d6+9 piercing plus serpentfolk venom"
abilities_bot:
  - name: "Raise Serpent"
    desc: "⬽ (Divine)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The bone prophet animates corpses of snakes, serpentfolk, or similar serpentine creatures within a 30-foot emanation. Any flesh on the bodies sloughs off, and they rise as skeletons. The bone prophet can raise one Large creature as a skeletal giant or up to three Medium creatures as skeletal champion; the equipment and attacks might be different depending on the corpses' possessions. These skeletons have the minion trait and are under the bone prophet's control; the bone prophet can give all these minions the same command with a single action that has the concentrate trait. Any skeletal minions that still remain after 10 minutes crumble to dust."
  - name: "Serpentfolk Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 26 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d4 poison damage and enfeebled 1 (1 round)"
  - name: "Stage 2"
    desc: "2d4 poison damage and enfeebled 1 (1 round)"
spellcasting:
  - name: "Divine Spontaneous Spells"
    desc: "DC 28, attack +20 - __Cantrips (4th)__ Detect Magic, Guidance, Light, Read Aura, Void Warp - __1st__ Bane, Command, Fear, Ventriloquism (4 slots) - __2nd__ Blood Vendetta, Darkness, Resist Energy, See the Unseen (4 slots) - __3rd__ Bind Undead, Blindness, Chilling Darkness, Vampiric Feast (4 slots) - __4th__ Fly, Harm, Read Omens, Talking Corpse (3 slots)"
  - name: "Occult Innate Spells"
    desc: "DC 28 - __1st__ Ventriloquism (at will) - __2nd__ Blur (self only; at will) - __3rd__ Illusory Disguise (at will) - __5th__ Illusory Scene, Suggestion - __6th__ Dominate"
  - name: "Rituals"
    desc: "DC 28 - __2nd__ Create Undead"
sourcebook: "_Monster Core_, page 305."
```

```encounter-table
name: Bone Prophet
creatures:
  - 1: Bone Prophet
```
