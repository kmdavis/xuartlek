---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dig-Widget"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/small
statblock: inline
name: "Dig-Widget"
level: 5
source: "Monster Core 2"
aon_id: "creature-4332"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4332"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Dig-Widget"
level: "Creature 5"
size: "Small"
trait_01: "Construct"
trait_02: "Mindless"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision, tremorsense (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +12, Athletics +9, Stealth +14, Thievery +15"
abilityMods: [2, 5, 1, -5, 0, -5]
abilities_top:
  - name: "Infiltration Tools"
    desc: "A dig-widget's face consists of an infiltrator thieves' toolkit. This toolkit can be salvaged from a destroyed dig-widget with a successful DC 20 Crafting check. On a failed check, the tools are destroyed."
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +10; __Ref__: +14; __Will__: +7"
hp: 65
health:
  - name: "HP"
    desc: "65; __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, mental, nonlethal attacks, paralyzed, poison, sickened, spirit, unconscious, vitality, void"
abilities_mid:
  - name: "Mechanical Vulnerability"
    desc: "A creature with expert proficiency in Thievery can attempt a check to Disable a Device to damage a dig-widget. The DC is 22, and each success deals 20 damage."
speed: "30 feet, burrow 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ drill +14 (fatal d10, finesse) __Damage__ 2d6+4 piercing plus 1d6 persistent bleed"
  - name: "Melee"
    desc: "⬻ corkscrew +14 (Finesse) __Damage__ 2d8+4 piercing"
abilities_bot:
  - name: "Fastening Leap"
    desc: "⬻ The dig-widget Leaps up 20 feet onto a creature or object and attempts a corkscrew Strike against it. If the Strike damages the target, the dig-widget attaches to the target (typically to the back of a creature). This is similar to Grabbing the creature, but the dig-widget moves with that creature rather than holding it in place. While attached, the dig-widget can't use its corkscrew. The dig-widget can be Shoved off, or it can detach itself with an Interact action."
  - name: "Sneak Attack"
    desc: "A dig-widget's Strikes deal an additional 1d6 precision damage to off-guard creatures. Widget Workshops The first dig-widget came from the workshops of a dwarven thieves' guild called Godak's Grifters, which used more advanced magical clockwork theories as a springboard for these simpler but no less effective contraptions. With their dig-widgets, the Grifters plagued the authorities of several dwarven settlements over the years. Their travels spread dig-widget technology, and numerous improvements have since led to faster and more reliable versions. Though upstanding dwarven mechanics have observed dig-widgets and recognized the complexity of the technology, they've steadfastly refused to adapt something with such an unscrupulous origin."
sourcebook: "_Monster Core 2_, page 105."
```

```encounter-table
name: Dig-Widget
creatures:
  - 1: Dig-Widget
```
