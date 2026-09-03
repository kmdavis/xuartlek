---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vulot"
tags:
  - pf2e/creature/level/21
  - pf2e/creature/trait/demon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/mythic
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/unique
  - pf2e/creature/trait/large
statblock: inline
name: "Vulot"
level: 21
source: "War of Immortals"
aon_id: "creature-3404"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3404"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "WoI"
name: "Vulot"
level: "Creature 21"
size: "Large"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Mythic"
trait_04: "Unholy"
trait_05: "Unique"
modifier: 38
perception:
  - name: "Perception"
    desc: "Perception +38; darkvision, many eyes in many places, [[srd/pf2e/compendium/spells/rank-6/truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]]; all languages spoken by their collective identities; telepathy 200 feet (unlimited range to other stolen identities worn by cultists of Vulot)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +43, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +40, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +40, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +40"
abilityMods: [4, 6, 4, 7, 7, 10]
abilities_top:
  - name: "Absolute Surety"
    desc: "Vulot is dependent on deception and charm to achieve their goals. If Vulot fails to deceive someone, for example failing the [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] check associated with a [[srd/pf2e/compendium/spells/rank-6/mislead|_mislead_]] spell to convince an observer that an action came from the duplicate, Vulot takes 4d6 mental damage. This damage ignores Vulot's usual immunity."
  - name: "Many Eyes in Many Places"
    desc: "Vulot can extend their senses through any cultist wearing one of their stolen identities as long as the cultist is in [[srd/pf2e/compendium/gm/planes#The Universe|the Universe]] or the [[srd/pf2e/compendium/gm/planes#Outer Rifts|Outer Rifts]]. Vulot can't maintain their attention through more than three cultists at one time. Vulot can't speak through these cultists."
ac: 46
armorclass:
  - name: "AC"
    desc: "46; __Fort__: +32; __Ref__: +35; __Will__: +38"
hp: 425
health:
  - name: "HP"
    desc: "425; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], mythic immunity; __Weaknesses__ cold iron 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 15"
abilities_mid:
  - name: "Another Face"
    desc: "When Vulot is reduced to 0 Hit Points, they regenerate themself from a stolen identity of their choice in 24 hours. If Vulot has no stolen identities remaining or is otherwise unable to reach them, they are killed permanently."
  - name: "Mythic Immunity"
    desc: "Vulot is immune to harmful spells cast by non-[[srd/pf2e/compendium/rules-elements/traits/war-of-immortals/mythic|mythic]] creatures, Strikes made with non-mythic weapons, and unarmed Strikes from non-mythic characters."
  - name: "Suffocated by a Thousand Breaths"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|incapacitation]]) 30 feet. Vulot's breath-stealing influence radiates out from their body, causing victims to feel like they are being smothered. Any creature that starts its turn within the aura must attempt a DC 41 Fortitude save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature becomes short of breath and is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] until the beginning of its next turn."
  - name: "Failure"
    desc: "The creature finds it very difficult to catch its breath. It can't speak or use [[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|auditory]] actions until the beginning of its next turn; this prevents it from casting spells that don't have the [[srd/pf2e/compendium/rules-elements/traits/player-core/subtle|subtle]] trait."
  - name: "Critical Failure"
    desc: "All the air immediately leaves the creature's lungs and it begins to [[srd/pf2e/books/player-core/chapter-8-playing-the-game/encounter-mode#Drowning and Suffocating|suffocate]]. When it succeeds at the saving throw to regain consciousness at the end of its turn, it becomes [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]] until it gets a full night's rest."
  - name: "Perfect Mimicry"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]])"
  - name: "Trigger"
    desc: "A spell is cast within 60 feet of Vulot"
  - name: "Effect"
    desc: "Vulot copies the spell and may cast it once by spending a Mythic Point within the next 24 hours. Vulot can't hold more than two copied spells at one time."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +37 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 4d8+14 slashing plus 2d6 bleed"
  - name: "Ranged"
    desc: "⬻ thought spike +37 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], range increment 120 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 4d6+14 mental plus steal thoughts"
abilities_bot:
  - name: "Mythic Power"
    desc: "3 Mythic Points _Recharge Spell_ ⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]])"
  - name: "Cost"
    desc: "1 Mythic Point"
  - name: "Effect"
    desc: "Vulot gains an additional use of any of their innate spells._Remove a Condition_ ⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]])"
  - name: "Cost"
    desc: "1 Mythic Point"
  - name: "Effect"
    desc: "Vulot removes any one condition currently affecting them."
  - name: "Steal Face"
    desc: "⬺"
  - name: "Cost"
    desc: "1 Mythic Point"
  - name: "Effect"
    desc: "Vulot makes a claw Strike. On a hit, Vulot attempts a Deception check against the target's Will DC to steal that creature's face; on a critical hit, Vulot treats the result of their Deception check as one degree of success higher. On a success, Vulot steals the target's face for 1d4 rounds (1 minute on a critical success); a creature whose face has been stolen isn't considered an ally by any creature."
  - name: "Steal Thoughts"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) Vulot's mental attacks can confuse and disorient. A creature struck by Vulot's thought spike must attempt a DC 44 Will save. A creature [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied]] by this effect is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to Vulot's Steal Face ability."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature becomes stupefied 1 for 1 round."
  - name: "Failure"
    desc: "The creature becomes stupefied 1 for 1 minute. If it's already stupefied, its stupefied value increases by 1 instead (to a maximum of stupefied 4)."
  - name: "Critical Failure"
    desc: "As failure, plus the creature is [[srd/pf2e/compendium/rules-elements/conditions#Confused|confused]] for 1 minute."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 44 - __Cantrips (10th)__ [[srd/pf2e/compendium/spells/cantrips/daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/figment|Figment]] - __5th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will) - __6th__ [[srd/pf2e/compendium/spells/rank-6/mislead|Mislead]] (×3), [[srd/pf2e/compendium/spells/rank-6/repulsion|Repulsion]] - __7th__ [[srd/pf2e/compendium/spells/rank-7/divine-decree|Divine Decree]] (×2) - __9th__ [[srd/pf2e/compendium/spells/rank-9/overwhelming-presence|Overwhelming Presence]] - __10th__ [[srd/pf2e/compendium/spells/rank-6/dominate|Dominate]], [[srd/pf2e/compendium/spells/rank-10/manifestation|Manifestation]], [[srd/pf2e/compendium/spells/rank-5/shadow-blast|Shadow Blast]] (×2) - __Constant (6th)__ [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]]"
  - name: "Rituals"
    desc: "DC 44 - __1st__ [[srd/pf2e/compendium/spells/rituals/demonic-pact|Demonic Pact]]"
sourcebook: "_War of Immortals_, page 177."
```

```encounter-table
name: Vulot
creatures:
  - 1: Vulot
```
