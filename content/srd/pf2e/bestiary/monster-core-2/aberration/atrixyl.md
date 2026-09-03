---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Atrixyl"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/medium
statblock: inline
name: "Atrixyl"
level: 11
source: "Monster Core 2"
aon_id: "creature-4089"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4089"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Atrixyl"
level: "Creature 11"
size: "Medium"
trait_01: "Aberration"
trait_02: "Rare"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; darkvision; true sin scent (precise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Elven|Elven]], [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]], Thassilonian"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +22, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +20, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +22, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +18, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +18, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +20, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +20, [[srd/pf2e/compendium/rules-elements/skills/lore|Sinspawn Lore]] +20, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +22, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +16, [[srd/pf2e/compendium/rules-elements/skills/lore|Thassilon Lore]] +20"
abilityMods: [7, 5, 4, 3, 1, 3]
abilities_top:
  - name: "True Sin Scent"
    desc: "An atrixyl can smell creatures that reflect or generally revel in any of the seven sins as defined by the ancient empire of Thassilon (envy, gluttony, greed, lust, pride, sloth, and wrath) within 60 feet as a precise sense and can also distinguish between different sins and creatures. These typically include sinspawn and certain [[srd/pf2e/compendium/gm/creature-families/demon|demons]], though the GM ultimately determines which creatures are appropriately sinful."
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +24; __Ref__: +21; __Will__: +18 +1 status to saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 190
health:
  - name: "HP"
    desc: "190; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Controlled|controlled]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]] 10; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]] 10"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Spell Break"
    desc: "⬲"
  - name: "Trigger"
    desc: "The atrixyl critically succeeds on a saving throw"
  - name: "Effect"
    desc: "The atrixyl shatters the portion of magic that would affect them and uses it to empower themself. The atrixyl gains temporary Hit Points equal to twice the triggering spell's rank and a +4 status bonus to damage rolls for 1 round."
speed: "30 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 2d12+10 bludgeoning plus Improved Push"
abilities_bot:
  - name: "Absorb Sin"
    desc: "⭓"
  - name: "Trigger"
    desc: "The atrixyl reduces a creature it can smell with its true sin scent to 0 Hit Points"
  - name: "Effect"
    desc: "The atrixyl regains 6d6 Hit Points."
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]]) The atrixyl takes on the appearance of any Medium [[srd/pf2e/compendium/rules-elements/traits/player-core/humanoid|humanoid]]. This doesn't change the atrixyl's Speed or their attack and damage modifiers with their Strikes but might change the damage type their Strikes deal."
  - name: "Insectile Agility"
    desc: "When the atrixyl [[srd/pf2e/compendium/rules-elements/actions/player-core#Leap|Leaps]], [[srd/pf2e/compendium/rules-elements/actions/player-core#High Jump|High Jumps]], or [[srd/pf2e/compendium/rules-elements/actions/player-core#Long Jump|Long Jumps]], they can increase horizontal and vertical distances traveled by up to 10 feet. They also treat falls as 50 feet shorter."
  - name: "Resonating Kick"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]]) The atrixyl makes a fist Strike. If the target is an [[srd/pf2e/compendium/rules-elements/traits/player-core/aberration|aberration]] or is capable of casting spells from the [[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]] tradition, this attack deals an additional 2d12 force damage."
  - name: "Roundhouse Smash"
    desc: "⬺ The atrixyl makes a fist Strike and compares the attack roll result to the AC of up to two foes, each of whom must be within the atrixyl's melee reach and adjacent to each other. Roll damage only once and apply it to each creature hit. This counts as two attacks for the atrixyl's multiple attack penalty. Mysterious Antiheroes Atrixyls disguise themselves as humanoids to help avoid attention and gather information discreetly about runewells. While many atrixyls remain aloof from society, some find themselves in the unlikely roles of antiheroes who protect those same humanoids from sinspawn and fleshwarpers alike."
sourcebook: "_Monster Core 2_, page 46."
```

```encounter-table
name: Atrixyl
creatures:
  - 1: Atrixyl
```
