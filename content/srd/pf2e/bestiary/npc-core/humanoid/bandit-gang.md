---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Bandit Gang"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Bandit Gang"
level: 7
source: "NPC Core"
aon_id: "creature-3432"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3432"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Bandit Gang"
level: "Creature 7"
size: "Gargantuan"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Troop"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +16, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +14, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +16, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +17, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +11, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +16"
abilityMods: [3, 5, 2, 1, 2, 3]
abilities_top:
  - name: "Lie in Wait"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/exploration|exploration]]) The troop can spend 10 minutes preparing the ground before combat to gain a +2 circumstance bonus to their initiative roll."
  - name: "Sudden Ambush"
    desc: "When the troop rolls initiative using [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] or [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]], they can use Stand and Deliver! as a free action."
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +15; __Ref__: +16; __Will__: +13"
hp: 120
health:
  - name: "HP"
    desc: "120 (4 segments); __Weaknesses__ area damage 8, splash damage 8"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; forest passage, troop movement"
abilities_bot:
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The bandits make a coordinated attack with their axes against each enemy in a 5-foot emanation with a DC 22 basic Reflex save. The damage depends on the number of actions. ⬻ 1d6+3 slashing damage ⬺ 2d6+9 slashing damage ⬽ 3d6+9 slashing damage"
  - name: "Forest Passage"
    desc: "The bandit ignores any difficult terrain caused by plants, such as bushes, vines, and undergrowth. __Launch Slings!__ ⬺ The bandits draw or reload their slings, then launch a volley of sling bullets. This is a 10-foot burst within 50 feet that deals 2d6+4 bludgeoning damage with a DC 22 basic Reflex save. When the troop is reduced to 2 or fewer segments, this area decreases to a 5-foot burst. __Stand and Deliver!__ ⬻ The troop attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Demoralize|Demoralize]] up to 4 creatures."
sourcebook: "_NPC Core_, page 22."
```

```encounter-table
name: Bandit Gang
creatures:
  - 1: Bandit Gang
```
