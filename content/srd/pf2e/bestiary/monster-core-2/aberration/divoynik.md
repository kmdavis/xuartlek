---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Divoynik"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Divoynik"
level: 3
source: "Monster Core 2"
aon_id: "creature-4343"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4343"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Divoynik"
level: "Creature 3"
size: "Medium"
trait_01: "Aberration"
trait_02: "Uncommon"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; two other languages; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +11, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +9, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +9, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +8, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +10"
abilityMods: [3, 3, 0, 1, 2, 4]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +6; __Ref__: +10; __Will__: +11"
hp: 45
health:
  - name: "HP"
    desc: "45; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|polymorph]]; __Weaknesses__ cracked mirror 3"
abilities_mid:
  - name: "Cracked Mirror"
    desc: "A divoynik has weakness 3 to physical attacks made by a creature whose form they're mimicking, and the mimicked creature gains weakness 3 to physical attacks made by the divoynik."
  - name: "Sudden Betrayal"
    desc: "A divoynik can always use [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] when rolling initiative, as long as at least one enemy doesn't know their true nature. On the first round of combat, if the divoynik rolled Deception for initiative, creatures that haven't acted are [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to the divoynik."
  - name: "Savor Anguish"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]])"
  - name: "Trigger"
    desc: "A creature within 30 feet of the divoynik fails a saving throw against an emotion effect"
  - name: "Effect"
    desc: "The divoynik feeds on their victim's mental distress, gaining 5 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Temporary Hit Points|temporary Hit Points]] for up to 1 minute. They can feed on a given creature's emotions only once every 24 hours."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d10+5 bludgeoning"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|polymorph]]) The divoynik can take on the specific appearance of any Small or Medium animal or humanoid they've seen. This doesn't change their Speed or their attack and damage bonuses with their Strikes, but it might change the damage type their Strikes deal (such as to slashing with a claw)."
  - name: "Window to the Soul"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) The divoynik meets the gaze of a creature within 60 feet whose form they've taken with their Change Shape ability. The target must attempt a DC 20 Will saving throw."
  - name: "Critical Success"
    desc: "The target is unaffected and immune for 24 hours."
  - name: "Success"
    desc: "The target is unaffected."
  - name: "Failure"
    desc: "The target is [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]] for 1 minute. Hostile actions do not end this fascination, but if the divoynik Changes Shape, moves out of range, or is no longer visible to the target, the fascination immediately ends. While fascinated, the target takes a –1 circumstance penalty to Will saves against the divoynik's spells and abilities."
  - name: "Critical Failure"
    desc: "As failure, and the divoynik can spend a free action to telepathically extract the answer to one question from the target. The target can attempt a DC 20 [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] check to attempt to evade the query and give misleading information. Transient Tormentors A divoynik delights in terrorizing their victims, typically taking calculated steps to reveal themself to their intended target long before the divoynik makes their move. Perhaps they allow the target a fleeting glimpse of their face in a crowd or a trace of movement from the corner of their eye, only to vanish before certainty can set in. In addition to providing the divoynik with opportunities to steal their victim's memories, this prolonged psychological assault often drives their victim into a state of extreme distrust and agitation, making the victim's apparent crimes all the more believable."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 20 - __3rd__ [[srd/pf2e/compendium/spells/rank-3/mind-reading|Mind Reading]] (at will)"
sourcebook: "_Monster Core 2_, page 116."
```

```encounter-table
name: Divoynik
creatures:
  - 1: Divoynik
```
