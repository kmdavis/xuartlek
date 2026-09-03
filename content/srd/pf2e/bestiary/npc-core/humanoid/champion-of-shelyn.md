---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Champion of Shelyn"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Champion of Shelyn"
level: 7
source: "NPC Core"
aon_id: "creature-3446"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3446"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Champion of Shelyn"
level: "Creature 7"
size: "Medium"
trait_01: "Holy"
trait_02: "Human"
trait_03: "Humanoid"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +17, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +16, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +14, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +15, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +12"
abilityMods: [4, 1, 2, 1, 2, 3]
abilities_top:
  - name: "Items"
    desc: "Crossbow (10 bolts), Half Plate, _+1 [[srd/pf2e/compendium/equipment/weapons/polearm/glaive|glaive]]_, [[srd/pf2e/compendium/equipment/adventuring-gear/religious-symbol-silver|religious symbol]] of Shelyn"
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +15; __Ref__: +12; __Will__: +15"
hp: 120
health:
  - name: "HP"
    desc: "120"
abilities_mid:
  - name: "Champion's Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) 15 feet. Any follower of Shelyn in the aura knows the champion is a champion of Shelyn. At the end of the champion's turn, each ally in the aura reduces its [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] value by 1. The aura can be suppressed or resumed with a single action, which has the [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]] trait, and ends if the champion falls [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]."
  - name: "Champion's Courage"
    desc: "When the champion becomes [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]], they reduce the condition value by 1 (to a minimum of 0)."
  - name: "Liberating Step"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]])"
  - name: "Trigger"
    desc: "An enemy damages, [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabs]], or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrains]] the champion's ally, and both are in the champion's aura"
  - name: "Effect"
    desc: "The champion frees an ally from restraint. If the trigger was an ally taking damage, the ally gains resistance 10 to all damage against the triggering damage. The ally can attempt to break free of effects grabbing, restraining, [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilizing]], or [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzing]] them. They either attempt a new save against one such effect that allows a save or attempt to [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]] from one effect as a free action. Whether or not it needed to escape, the ally can then Step as a free action if it's able to move."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _glaive_ +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/forceful|Forceful]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|Reach]]) __Damage__ 1d8+10 slashing plus 1d6 persistent vitality"
  - name: "Melee"
    desc: "⬻ fist +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+10 bludgeoning"
  - name: "Ranged"
    desc: "⬻ crossbow +14 (range increment 120 feet, reload 1) __Damage__ 1d8+6 piercing"
abilities_bot:
  - name: "Champion Devotion Spells"
    desc: "DC 22, 2 Focus Points - __4th__ [[srd/pf2e/compendium/spells/focus/lay-on-hands|Lay on Hands]], [[srd/pf2e/compendium/spells/focus/protectors-sacrifice|Protector's Sacrifice]]"
  - name: "Blessed Weapon"
    desc: "If a champion's glaive Strike is a critical hit, the weapon deals an additional 1d6 persistent vitality damage, and they can force the target to move 5 feet in a direction of their choice."
  - name: "Smite"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]]) The champion chooses one enemy they can see. Their Strikes against that enemy gain a +4 status bonus to damage, or +8 if the target is [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]. This benefit lasts until the start of the champion's next turn, but if the target takes a hostile action against the champion or one of their allies, the duration is extended until the end of the target's next turn (this can be extended indefinitely if the target keeps taking hostile actions on subsequent rounds). Champion Causes Champions represent the martial forces tied to the various faiths all around Golarion. You can customize a champion to a different deity by swapping in their deity's favored weapon, selecting an appropriate blessing of the devoted, and choosing a cause fitting that deity's sanctification options. Use that cause to determine the champion's sanctification and champion's reaction."
sourcebook: "_NPC Core_, page 32."
```

```encounter-table
name: Champion of Shelyn
creatures:
  - 1: Champion of Shelyn
```
