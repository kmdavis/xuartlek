---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Exiled Revolutionary"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Exiled Revolutionary"
level: 10
source: "NPC Core"
aon_id: "creature-3519"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3519"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Exiled Revolutionary"
level: "Creature 10"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; (20 to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]])"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +18, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +19, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +19, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +17, [[srd/pf2e/compendium/rules-elements/skills/lore|Lore]] +22, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +20, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +20, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +18"
abilityMods: [4, 5, 0, 3, 2, 4]
abilities_top:
  - name: "Former Courtier"
    desc: "An exiled revolutionary remembers well their former realm. In their home realm, be it a manor, castle, or capital city, the exiled revolutionary gains a +4 circumstance bonus to Perception checks and Will saves, and to [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]], [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]], [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]], and [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] checks, and is a 12th-level challenge in the arena of noble politics."
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/weapons/bow/composite-longbow|composite longbow]]_ (20 arrows), Leather Armor, _+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/sword/longsword|longsword]]_, signet ring, [[srd/pf2e/compendium/equipment/adventuring-gear/thieves-toolkit-infiltrator-picks|Thieves' Toolkit]], Wyvern Poison (2)"
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +17; __Ref__: +20; __Will__: +17"
hp: 140
health:
  - name: "HP"
    desc: "140"
abilities_mid:
  - name: "Follow Me"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) 20 feet. This aura is active only while in the exiled revolutionary's home realm, as they share knowledge to avoid guard patrols and get past checkpoints. Any ally in the aura gets a +2 circumstance bonus to [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] and [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] checks. __It's… You!__ ([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) When the exiled revolutionary sees or hears someone who was part of their downfall in person, they break cover and attack their betrayer immediately, even if their actions would doom them and their allies. The revolutionary must succeed at a DC 35 Will save or be [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]] by their betrayer and unable to cease targeting them exclusively until the betrayer is defeated. An ally can convince the revolutionary to forgo their vengeance with a DC 30 [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] check to make a [[srd/pf2e/compendium/rules-elements/actions/player-core#Request|Request]]. This lasts for 1 minute, but talking the revolutionary down after that time requires more thorough engagement."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _longsword_ +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]]) __Damage__ 2d8+10 slashing"
  - name: "Melee"
    desc: "⬻ fist +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+10 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _composite longbow_ +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range increment 100 feet, reload 0, [[srd/pf2e/compendium/rules-elements/traits/player-core/volley|volley 30 feet]]) __Damage__ 1d8+8 piercing"
abilities_bot:
  - name: "Darting Feint"
    desc: "⬺ The exiled revolutionary [[srd/pf2e/compendium/rules-elements/actions/player-core#Feint|Feints]], Steps, and Strikes in any order."
  - name: "Sneak Attack"
    desc: "The exiled revolutionary deals an additional 2d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures. Betraying The Betrayed Exiled revolutionaries can make for valuable allies, especially if their goals align with the PCs. However, the exiled revolutionary has been a victim of extreme betrayal and constantly guards against it. PCs should take care when considering going back on their word with an exiled revolutionary. Should anyone act in a way that the exiled revolutionary might perceive as a betrayal, the revolutionary will dedicate their life to avenging the perceived transgression, even becoming a villainous instrument of evil should that become necessary."
sourcebook: "_NPC Core_, page 85."
```

```encounter-table
name: Exiled Revolutionary
creatures:
  - 1: Exiled Revolutionary
```
