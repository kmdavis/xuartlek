---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Loan Shark"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Loan Shark"
level: 2
source: "NPC Core"
aon_id: "creature-3426"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3426"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Loan Shark"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/lore|Accounting Lore]] +17, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +9, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +8, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +8, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +8, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +15"
abilityMods: [3, 0, 1, 2, 2, 4]
abilities_top:
  - name: "Business Savvy"
    desc: "When making monetary deals, the loan shark gets a +8 circumstance bonus to [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] checks, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] checks, and their Perception DC."
  - name: "Loan Specialist"
    desc: "For encounters involving monetary deals, the loan shark is a 7th-level challenge."
  - name: "Items"
    desc: "Breastplate, dragon-headed cane (functions as a [[srd/pf2e/compendium/equipment/weapons/club/staff|staff]])"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +7; __Ref__: +6; __Will__: +10"
hp: 25
health:
  - name: "HP"
    desc: "25"
abilities_mid:
  - name: "Never off the Hook"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) 60 feet. Creatures in the aura who owe the loan shark money take a –3 circumstance penalty to their Will DC against the loan shark's attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Demoralize|Demoralize]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Coerce|Coerce]] them and can't reduce their frightened value below 1 while in the aura."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dragon-headed cane +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/two-hand|two-hand d8]]) __Damage__ 1d4+5 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+5 bludgeoning __Interest is Due!__ ⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]])"
abilities_bot:
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The loan shark commands an ally within 30 feet to attack a creature who owes the loan shark money. The ally can use a reaction to Strike the debtor, dealing an additional 1d6 mental damage."
sourcebook: "_NPC Core_, page 19."
```

```encounter-table
name: Loan Shark
creatures:
  - 1: Loan Shark
```
