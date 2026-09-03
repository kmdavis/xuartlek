---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Warmonger"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Warmonger"
level: 10
source: "NPC Core"
aon_id: "creature-3620"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3620"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Warmonger"
level: "Creature 10"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +24, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +20, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +19, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +14, [[srd/pf2e/compendium/rules-elements/skills/lore|Warfare Lore]] +21"
abilityMods: [6, 4, 5, 1, 0, 0]
abilities_top:
  - name: "War Ready"
    desc: "The warmonger can always roll [[srd/pf2e/compendium/rules-elements/skills/lore|Warfare Lore]] for initiative."
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/axe/battle-axe|battle axe]]_ (2), _+1 [[srd/pf2e/compendium/equipment/weapons/bow/composite-longbow|composite longbow]]_ (10 arrows), _+1 [[srd/pf2e/compendium/equipment/armor#Hide Armor|hide armor]]_"
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +21; __Ref__: +20; __Will__: +16"
hp: 200
health:
  - name: "HP"
    desc: "200"
abilities_mid:
  - name: "Pain Training"
    desc: "The warmonger treats the value of any [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/conditions#Dying|dying]], [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]], [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]], and [[srd/pf2e/compendium/rules-elements/conditions#Wounded|wounded]] conditions affecting them as 1 lower. The warmonger still has the condition and must remove it normally."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "30 feet, climb 10 feet, swim 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _battle axe_ +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 2d8+12 slashing"
  - name: "Melee"
    desc: "⬻ fist +22 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+12 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _composite longbow_ +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 100 feet, reload 0, [[srd/pf2e/compendium/rules-elements/traits/player-core/volley|volley 30 feet]]) __Damage__ 1d8+9 piercing"
abilities_bot:
  - name: "Patch and Set"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/healing|Healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Requirements"
    desc: "The warmonger has a hand free"
  - name: "Effect"
    desc: "The warmonger grits their teeth and ties off a wound or sets a bone or joint. They regain 20 Hit Points."
  - name: "Power Through"
    desc: "⬺"
  - name: "Requirements"
    desc: "The warmonger is wielding two melee weapons and isn't [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]]"
  - name: "Effect"
    desc: "The warmonger attempts up to three melee Strikes against different creatures. These count toward the warmonger's multiple attack penalty normally, but the penalty doesn't increase until after all the attacks. The warmonger overexerts themself with the attacks, becoming fatigued. The warmonger can attempt a DC 30 Fortitude save to recover from this fatigued condition at the start of each of their turns."
  - name: "Sight Prey"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]]) The warmonger singles out one enemy to bring down with ranged attacks until the end of the current turn. The warmonger's ranged Strikes against that creature gain a +1 circumstance bonus to the attack roll and deal an extra 3d6 precision damage. Each time the warmonger hits that creature with a ranged Strike, the creature takes a –10-foot penalty to its Speeds for 1 minute and falls 20 feet if it's flying."
  - name: "War Cry"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]])"
  - name: "Frequency"
    desc: "once per hour"
  - name: "Trigger"
    desc: "The warmonger critically hits or knocks out an enemy"
  - name: "Effect"
    desc: "The warmonger screams a battle cry. Each ally in a 30-foot emanation that hears it deals an additional 1d6 damage with its Strikes for 1 round."
sourcebook: "_NPC Core_, page 161."
```

```encounter-table
name: Warmonger
creatures:
  - 1: Warmonger
```
