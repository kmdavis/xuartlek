---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Yeti"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Yeti"
level: 5
source: "Monster Core"
aon_id: "creature-3247"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3247"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Yeti"
level: "Creature 5"
size: "Large"
trait_01: "Humanoid"
trait_02: "Uncommon"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +14, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +12, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +11"
abilityMods: [5, 2, 4, -1, 4, -1]
abilities_top:
  - name: "Snowblind"
    desc: "When [[srd/pf2e/compendium/rules-elements/actions/player-core#Hide|Hiding]], the yeti is [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] by any snowfall, even if it's not thick enough to make other creatures concealed."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +15; __Ref__: +11; __Will__: +13 +4 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]] and [[srd/pf2e/compendium/rules-elements/traits/gm-core/dream|dreams]]"
hp: 115
health:
  - name: "HP"
    desc: "115; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 10"
abilities_mid:
  - name: "Nightmare Guardian"
    desc: "Yetis gain a +4 status bonus to saves against fear and against spells and abilities that affect dreams. A yeti who falls prey to a supernatural nightmare loses this ability and becomes permanently enraged, gaining a +1 status bonus to attack and damage rolls and a –1 status penalty to AC."
  - name: "Vanish"
    desc: "⬲"
  - name: "Trigger"
    desc: "The yeti is [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]] or [[srd/pf2e/compendium/rules-elements/conditions#Undetected|undetected]] while not in combat, and a creature would observe it"
  - name: "Effect"
    desc: "The yeti Strides or [[srd/pf2e/compendium/rules-elements/actions/player-core#Climb|Climbs]] up to half its Speed to a location where it can Hide, then Hides. If its new [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] check result meets or exceeds the triggering creature's Perception DC, the yeti remains hidden."
speed: "35 feet, climb 20 feet; arctic passage"
attacks:
  - name: "Melee"
    desc: "⬻ claw +15 __Damage__ 2d10+5 slashing"
abilities_bot:
  - name: "Arctic Passage"
    desc: "The yeti ignores difficult terrain caused by ice or snow."
  - name: "Grisly Arrival"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]])"
  - name: "Trigger"
    desc: "The yeti hits a creature in the first round of combat and the yeti was [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]] from that creature at the start of combat"
  - name: "Effect"
    desc: "Each enemy within 30 feet that witnesses the attack (including the target of the attack) must attempt a DC 23 Will save. On a failure, the creature is [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened 2]]; on a critical failure, it's frightened 4."
  - name: "Rend"
    desc: "⬻ claw Yeti Crafts Lone exiles of yeti clans have little use for treasure and leave the gear of their slain victims behind, where it is quickly covered by snowfall. Clan-based yetis, on the other hand, create beautifully carved stonework, some of which they shape into protective talismans of rare beauty"
sourcebook: "_Monster Core_, page 354."
```

```encounter-table
name: Yeti
creatures:
  - 1: Yeti
```
