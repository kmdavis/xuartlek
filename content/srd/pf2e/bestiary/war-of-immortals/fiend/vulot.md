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
    desc: "Perception +38; darkvision, many eyes in many places, _truesight_"
languages: "Chthonian, Common, Draconic, Empyrean; all languages spoken by their collective identities; telepathy 200 feet (unlimited range to other stolen identities worn by cultists of Vulot)"
skills:
  - name: "Skills"
    desc: "Deception +43, Diplomacy +40, Society +40, Thievery +40"
abilityMods: [4, 6, 4, 7, 7, 10]
abilities_top:
  - name: "Absolute Surety"
    desc: "Vulot is dependent on deception and charm to achieve their goals. If Vulot fails to deceive someone, for example failing the Deception check associated with a _mislead_ spell to convince an observer that an action came from the duplicate, Vulot takes 4d6 mental damage. This damage ignores Vulot's usual immunity."
  - name: "Many Eyes in Many Places"
    desc: "Vulot can extend their senses through any cultist wearing one of their stolen identities as long as the cultist is in the Universe or the Outer Rifts. Vulot can't maintain their attention through more than three cultists at one time. Vulot can't speak through these cultists."
ac: 46
armorclass:
  - name: "AC"
    desc: "46; __Fort__: +32; __Ref__: +35; __Will__: +38"
hp: 425
health:
  - name: "HP"
    desc: "425; __Immunities__ mental, mythic immunity; __Weaknesses__ cold iron 10, holy 15"
abilities_mid:
  - name: "Another Face"
    desc: "When Vulot is reduced to 0 Hit Points, they regenerate themself from a stolen identity of their choice in 24 hours. If Vulot has no stolen identities remaining or is otherwise unable to reach them, they are killed permanently."
  - name: "Mythic Immunity"
    desc: "Vulot is immune to harmful spells cast by non-mythic creatures, Strikes made with non-mythic weapons, and unarmed Strikes from non-mythic characters."
  - name: "Suffocated by a Thousand Breaths"
    desc: "(aura, incapacitation) 30 feet. Vulot's breath-stealing influence radiates out from their body, causing victims to feel like they are being smothered. Any creature that starts its turn within the aura must attempt a DC 41 Fortitude save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature becomes short of breath and is off-guard until the beginning of its next turn."
  - name: "Failure"
    desc: "The creature finds it very difficult to catch its breath. It can't speak or use auditory actions until the beginning of its next turn; this prevents it from casting spells that don't have the subtle trait."
  - name: "Critical Failure"
    desc: "All the air immediately leaves the creature's lungs and it begins to suffocate. When it succeeds at the saving throw to regain consciousness at the end of its turn, it becomes fatigued until it gets a full night's rest."
  - name: "Perfect Mimicry"
    desc: "⬲ (magical, mental)"
  - name: "Trigger"
    desc: "A spell is cast within 60 feet of Vulot"
  - name: "Effect"
    desc: "Vulot copies the spell and may cast it once by spending a Mythic Point within the next 24 hours. Vulot can't hold more than two copied spells at one time."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +37 (Agile, Finesse, Magical, Unholy) __Damage__ 4d8+14 slashing plus 2d6 bleed"
  - name: "Ranged"
    desc: "⬻ thought spike +37 (Magical, Mental, range increment 120 feet, Unholy) __Damage__ 4d6+14 mental plus steal thoughts"
abilities_bot:
  - name: "Mythic Power"
    desc: "3 Mythic Points _Recharge Spell_ ⬻ (concentrate)"
  - name: "Cost"
    desc: "1 Mythic Point"
  - name: "Effect"
    desc: "Vulot gains an additional use of any of their innate spells._Remove a Condition_ ⬻ (concentrate)"
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
    desc: "(Emotion, Mental) Vulot's mental attacks can confuse and disorient. A creature struck by Vulot's thought spike must attempt a DC 44 Will save. A creature stupefied by this effect is off-guard to Vulot's Steal Face ability."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature becomes stupefied 1 for 1 round."
  - name: "Failure"
    desc: "The creature becomes stupefied 1 for 1 minute. If it's already stupefied, its stupefied value increases by 1 instead (to a maximum of stupefied 4)."
  - name: "Critical Failure"
    desc: "As failure, plus the creature is confused for 1 minute."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 44 - __Cantrips (10th)__ Daze, Figment - __5th__ Translocate (at will) - __6th__ Mislead (×3), Repulsion - __7th__ Divine Decree (×2) - __9th__ Overwhelming Presence - __10th__ Dominate, Manifestation, Shadow Blast (×2) - __Constant (6th)__ Truesight"
  - name: "Rituals"
    desc: "DC 44 - __1st__ Demonic Pact"
sourcebook: "_War of Immortals_, page 177."
```

```encounter-table
name: Vulot
creatures:
  - 1: Vulot
```
