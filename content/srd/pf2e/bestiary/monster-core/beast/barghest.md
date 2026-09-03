---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Barghest"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Barghest"
level: 4
source: "Monster Core"
aon_id: "creature-2846"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2846"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Barghest"
level: "Creature 4"
size: "Medium"
trait_01: "Beast"
trait_02: "Unholy"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]], [[srd/pf2e/compendium/rules-elements/languages#Goblin|Goblin]], [[srd/pf2e/compendium/rules-elements/languages#Jotun|Jotun]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +11, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +9, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +11, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +10, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +12"
abilityMods: [5, 2, 3, 2, 2, 3]
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +11; __Ref__: +12; __Will__: +8"
hp: 50
health:
  - name: "HP"
    desc: "50; __Resistances__ physical 5 (except cold iron); __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 5"
abilities_mid:
  - name: "Primal Hunt"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|teleportation]])"
  - name: "Trigger"
    desc: "A creature within the barghest's reach takes a [[srd/pf2e/compendium/rules-elements/traits/player-core/move|move]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|teleportation]] action"
  - name: "Effect"
    desc: "After the triggering action, the barghest can teleport up to 60 feet to a space adjacent to that creature."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 2d8+5 piercing plus Knockdown"
  - name: "Melee"
    desc: "⬻ claw +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 2d6+5 slashing plus unhealing wound"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The barghest takes on the shape of a [[srd/pf2e/compendium/rules-elements/traits/player-core/humanoid|humanoid]], a dog, or its true form. Their size changes to match the new form. When the barghest is a humanoid, their claw Strike deals bludgeoning damage and they lose their jaws Strike. When the barghest is a dog, their Speed changes to 35 feet. Each individual barghest has only one humanoid form and one dog form."
  - name: "Unhealing Wound"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) A creature damaged by the barghest's claws must succeed at a DC 21 Fortitude save or be cursed. The cursed creature can't regain Hit Points except via magic until it returns to maximum Hit Points. The creature can attempt a new saving throw against the curse every 24 hours. Canine Rivalries In addition to their adversarial relationships with other barghests, the beasts are hated by mundane dogs and wolves. They fit in more easily among intelligent lupine beasts like warg and werewolves, with wild barghests leading those packs or occasionally accepting the leadership of a powerful specimen like a witchwarg. The Origins Of Barghests Many different legends purport to explain the origins of barghests, invoking everyone from Lamashtu to the fey's Wild Hunt. Although of interest to scholars, barghests themselves have little concern for these legends other than adding their supposed creators as prey to aspire to."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 21 - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/figment|Figment]], [[srd/pf2e/compendium/spells/cantrips/light|Light]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/invisibility|Invisibility]], [[srd/pf2e/compendium/spells/rank-2/mist|Mist]]"
sourcebook: "_Monster Core_, page 38."
```

```encounter-table
name: Barghest
creatures:
  - 1: Barghest
```
