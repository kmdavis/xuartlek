---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mummy Guardian"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/mummy
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Mummy Guardian"
level: 6
source: "Monster Core"
aon_id: "creature-3101"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3101"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Mummy Guardian"
level: "Creature 6"
size: "Medium"
trait_01: "Mummy"
trait_02: "Undead"
trait_03: "Unholy"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision"
languages: "Necril; plus any one language they knew while alive"
skills:
  - name: "Skills"
    desc: "Athletics +15, Stealth +11"
abilityMods: [4, 0, 2, -2, 4, 2]
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +14; __Ref__: +10; __Will__: +16"
hp: 125
health:
  - name: "HP"
    desc: "125 (void healing); __Immunities__ bleed, death effects, disease, paralyzed, poison, unconscious; __Weaknesses__ alchemical 5 (see alchemical weakness), fire 5"
abilities_mid:
  - name: "Alchemical Weakness"
    desc: "The guardian's weakness to alchemical items not only applies to damage from alchemical items, but the guardian also takes 5 damage when splashed with non-damaging alchemical items or dosed with alchemical poisons, even if they're immune to their other effects."
  - name: "Blighted Consumption"
    desc: "⬲ (curse, divine, poison)"
  - name: "Trigger"
    desc: "A creature within 30 feet eats or drinks (including an alchemical item or potion)"
  - name: "Effect"
    desc: "The food or drink burns like the caustic substances fed to the mummy before its death. If the creature fails a DC 24 Fortitude save, they become sickened 2 after they finish the consumption and can't reduce their sickened condition while within 30 feet of any mummy."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +16 (Agile) __Damage__ 2d10+7 bludgeoning plus Choking Pain"
abilities_bot:
  - name: "Choking Pain"
    desc: "⬻ (Divine, Illusion, Mental, Void)"
  - name: "Requirements"
    desc: "The mummy's last action was a successful fist Strike"
  - name: "Effect"
    desc: "The mummy shares the pain of its dying moments with the target of that Strike. That creature takes 3d8 void damage with a DC 24 basic Will save. If the creature critically fails the saving throw, it can't speak for 1 round, including to Cast a Spell."
sourcebook: "_Monster Core_, page 234."
```

```encounter-table
name: Mummy Guardian
creatures:
  - 1: Mummy Guardian
```
