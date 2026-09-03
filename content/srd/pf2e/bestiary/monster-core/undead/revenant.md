---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Revenant"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/medium
statblock: inline
name: "Revenant"
level: 6
source: "Monster Core"
aon_id: "creature-3167"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3167"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Revenant"
level: "Creature 6"
size: "Medium"
trait_01: "Undead"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision, sense murderer"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; any one spoken in life by their murderer (typically [[srd/pf2e/compendium/rules-elements/languages#Common|Common]])"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +14"
abilityMods: [5, 3, 4, 0, 3, 2]
abilities_top:
  - name: "Sense Murderer"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/scrying|scrying]]) A revenant knows the direction of their murderer (as long as both are on the same plane), but not the distance."
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +14; __Ref__: +13; __Will__: +17"
hp: 115
health:
  - name: "HP"
    desc: "115 (void healing); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Resistances__ physical 5 (except slashing)"
abilities_mid:
  - name: "Self-Loathing"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) If a revenant sees their own reflection or any object that was important to them in life, they must attempt a DC 25 Will save."
  - name: "Critical Success"
    desc: "The revenant is unaffected and can no longer be affected by that reflection or object in this way."
  - name: "Success"
    desc: "The revenant is distracted by self-loathing and becomes [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]] for 1 round."
  - name: "Failure"
    desc: "The revenant becomes [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]] by the source that triggered their self-loathing and does everything they can to destroy it until the end of the revenant's next turn."
  - name: "Critical Failure"
    desc: "The revenant becomes [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] as long as the source of their self-loathing is apparent, until they're attacked, or until they see their murderer."
  - name: "Undying Vendetta"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]) If the revenant's murderer dies, the revenant is immediately destroyed. A revenant that can't sense their murderer must attempt a DC 11 flat check once every 24 hours to avoid becoming [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] and [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]; they immediately rise again once they can sense their murderer. A murderer who becomes [[srd/pf2e/compendium/rules-elements/traits/player-core/undead|undead]] does not trigger the revenant's destruction until the murderer is finally destroyed. The revenant gains a +2 status bonus to checks and DCs against their murderer."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d8+5 slashing plus Grab"
abilities_bot:
  - name: "Baleful Shriek"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The revenant wails horribly. Each creature within a 60-foot burst must attempt a DC 23 Will save. Regardless of the outcome of their saving throw affected creatures are then immune to Baleful Shriek for 1 hour. The revenant's murderer never improves their degree of success due to this ability's incapacitation trait. The revenant can't use Baleful Shriek again for 1d4 rounds."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened 2]]."
  - name: "Failure"
    desc: "The creature is frightened 2 and [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]] for 1 round."
  - name: "Critical Failure"
    desc: "The creature is frightened 3 and paralyzed for 1d4 rounds."
  - name: "Constrict"
    desc: "⬻ 2d6+5 bludgeoning, DC 24 Exceptions To Evil While most undead are indiscriminately malevolent, revenants are not—these unusual stalkers rise not out of a sense of cruelty or hatred of the living, but spontaneously from the need for vengeance following a deep betrayal. One can avoid a revenant's wrath by simply getting out of its way—unless you happen to be its reason for unlife!"
sourcebook: "_Monster Core_, page 292."
```

```encounter-table
name: Revenant
creatures:
  - 1: Revenant
```
