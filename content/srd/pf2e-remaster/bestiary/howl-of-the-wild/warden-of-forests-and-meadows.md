---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Warden of Forests and Meadows"
tags:
  - pf2e/creature/level/22
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/unique
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Warden of Forests and Meadows"
level: 22
source: "Howl of the Wild"
aon_id: "creature-3326"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3326"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Warden of Forests and Meadows"
level: "Creature 22"
size: "Gargantuan"
trait_01: "Beast"
trait_02: "Unique"
trait_03: "Wood"
modifier: 36
perception:
  - name: "Perception"
    desc: "Perception +36; greater darkvision, scent (imprecise) 1 mile"
languages: "voice of nature"
skills:
  - name: "Skills"
    desc: "Acrobatics +40, Deception +44, Diplomacy +40, Intimidation +42, Nature +36, Society +39, Stealth +42, Survival +36, Thievery +40"
abilityMods: [7, 10, 8, 11, 8, 12]
abilities_top:
  - name: "Voice of Nature"
    desc: ""
  - name: "Warden's Crown"
    desc: ""
ac: 48
armorclass:
  - name: "AC"
    desc: "48; __Fort__: +34; __Ref__: +42; __Will__: +36 +1 to all saves vs. primal"
hp: 435
health:
  - name: "HP"
    desc: "435"
abilities_mid:
  - name: "Wild Trickery"
    desc: "⬲ (mental, primal)"
  - name: "Trigger"
    desc: "An enemy within 60 feet targets the warden with an attack, spell, or other ability"
  - name: "Effect"
    desc: "The triggering creature must attempt a DC 45 Will save. If it fails, the warden redirects the ability to target a different creature in range with a burst of mental laughter; this has no effect if there are no other eligible targets. The triggering creature is then temporarily immune for 24 hours unless it critically failed."
speed: "60 feet, climb 30 feet; forest passage"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +38 (Finesse, Magical, reach 15 feet) __Damage__ 4d10+15 piercing"
  - name: "Melee"
    desc: "⬻ horned crown +40 (Finesse, Magical, reach 10 feet) __Damage__ 4d8+15 piercing plus 2d6 persistent poison"
  - name: "Melee"
    desc: "⬻ claw +40 (Agile, Finesse, Magical, reach 15 feet) __Damage__ 4d6+15 slashing"
  - name: "Ranged"
    desc: "⬻ fox's laughter +40 (Magical, range 120 feet) __Damage__ 4d10 sonic plus 3d6 mental"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Polymorph, Primal) The warden transforms his size to Tiny, Small, Medium, or Huge (changing his reach to 0 feet for Tiny, 5 feet for Medium or Large, and 10 feet for Huge). The warden retains his shape but can change his color to any seasonal array."
  - name: "Forest Passage"
    desc: "The Warden of Forests and Meadows ignores difficult terrain and greater difficult terrain from non-magical foliage."
  - name: "Fox's Wager"
    desc: "⬻ (Concentrate, Mental, Primal) The warden grants a boon to a willing creature he can see other than himself, requesting that the creature promise to use the granted power to destroy or undermine the creations of civilization. The target gains a +1 status bonus to attack rolls and a +5 status bonus to damage against constructs, objects, and structures constructed by humanoids. It also gains a +2 status bonus to Stealth checks against humanoids. The warden can have only one wager granted at a time. The wager ends if the target is captured or dies."
  - name: "Idyllic Panorama"
    desc: "⬻ (Concentrate, Primal)"
  - name: "Frequency"
    desc: "once per hour"
  - name: "Effect"
    desc: "The warden creates an area of peaceful calm. This is identical to a 5th-rank _mirage_ depicting a peaceful meadow or forest, except the area is a 200-foot burst. While within the area of an Idyllic Panorama, the warden has significant control over the senses of creatures within the area and can cast _mislead_ and 2nd-rank _silence_ at will."
  - name: "Magical Pounce"
    desc: "⬻ The warden Strides up to his Speed, Leaps up to his Speed, or casts _translocate_; at the end of that movement, the warden Strikes. If the warden began this action hidden, he remains hidden until after this ability's Strike."
  - name: "Sneak Attack"
    desc: "The warden deals an additional 3d6 precision damage to off-guard creatures."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 45, attack +41 - __Cantrips (10th)__ Figment, Light - __4th__ Translocate (at will) - __10th__ Manifestation, Petal Storm - __Constant (7th)__ Truespeech, Veil of Privacy"
sourcebook: "_Howl of the Wild_, page 205."
```

```encounter-table
name: Warden of Forests and Meadows
creatures:
  - 1: Warden of Forests and Meadows
```
