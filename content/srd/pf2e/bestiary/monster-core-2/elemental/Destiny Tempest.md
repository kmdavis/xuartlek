---
noteType: pf2eMonster
aliases: "Destiny Tempest"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/air
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/medium
statblock: inline
name: "Destiny Tempest"
level: 13
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4324"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Destiny Tempest"
level: "Creature 13"
size: "Medium"
trait_01: "Air"
trait_02: "Elemental"
modifier: 26
perception:
  - name: "Perception"
    desc: "+26; greater darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Sussuran|Sussuran]]; (can't speak any language); telepathy 100 feet, [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +25, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +21, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +26, [[srd/pf2e/compendium/rules-elements/skills/Lore|Dimension of Time Lore]] +25, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +27"
abilityMods: [4, 8, 6, 8, 7, 7]
ac: 34
armorclass:
  - name: "AC"
    desc: "34; __Fort__: +19; __Ref__: +24; __Will__: +26"
hp: 230
health:
  - name: "HP"
    desc: "230; __Immunities__ [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|bleed]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sleep|sleep]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Force|force]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|spirit]] 10"
abilities_mid:
  - name: "Ebbing Cloud"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|occult]]) 15 feet. Destiny tempests surround themselves with thoughts of averted fates, creating a thick metaphysical soup that cloys the mind and clouds ambition. Creatures in the area moving toward the destiny tempest treat the area as difficult terrain."
  - name: "No Breath"
    desc: "Destiny tempests do not need to breathe."
  - name: "Unspeakable Insights"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|occult]]) Touching a destiny tempest's mind even briefly grants a powerful and painful awareness of uncharted pasts, presents, and futures, too impossibly vast for mortal minds to conceptualize or contain. Whenever a creature targets the destiny tempest with a magical mental effect, it must attempt a DC 33 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected and becomes immune to unspeakable insights for 24 hours."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature takes 3d6 mental damage."
  - name: "Critical Failure"
    desc: "The creature takes 6d6 mental damage and becomes [[srd/pf2e/compendium/rules-elements/Conditions#Confused|confused]] for 1 round."
  - name: "Center of Destiny"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|teleportation]])"
  - name: "Trigger"
    desc: "A creature within 30 feet benefits from a [[srd/pf2e/compendium/rules-elements/traits/player-core/Fortune|fortune]] effect"
  - name: "Effect"
    desc: "Shadows surround and steal away the destiny tempest, who reappears in an open space adjacent to the triggering creature."
speed: "25 feet, fly 60 feet; swiftness"
attacks:
  - name: "Melee"
    desc: "⬻ slithering whisper +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Air|Air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 2d8+10 bludgeoning plus 1d8 mental and sound without voice"
  - name: "Ranged"
    desc: "⬻ umbral breath +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Air|Air]], range increment 30 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|Void]]) __Damage__ 4d10 void"
abilities_bot:
  - name: "Divergent Potential"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fortune|Fortune]]) The destiny tempest chooses two creatures it can see within 60 feet and rolls two slithering whisper Strikes, one against each creature. After seeing the outcomes of the two Strikes, the destiny tempest chooses one of the two targets to pursue, [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Immunity, Weakness, and Resistance|Flies]] up to 60 feet to reach the chosen target, and uses the result of the chosen Strike; the other Strike is lost. If the destiny tempest is prevented from reaching its chosen target, the attack is prevented and the chosen Strike is lost."
  - name: "Sound Without Voice"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Air|Air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]]) A creature damaged by the destiny tempest's slithering whisper Strike must succeed at a DC 33 basic Will save or become [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened 2]]."
  - name: "Swiftness"
    desc: "A destiny tempest's movement doesn't trigger reactions. Hushed Voices On the [[srd/pf2e/compendium/gm/Planes#Plane of Air|Plane of Air]], many creatures communicate through telepathy, shared dreams, or illusory rebuses. Though destiny tempests are telepathic and can magically understand most languages, they prefer to convey their thoughts and ideas metaphorically by shaping the clouds and currents of the Plane of Air to act out elaborate, moving stories and plays. Sometimes these animated clouds retain a bit of magic, becoming [[srd/pf2e/bestiary/rage-of-elements/elemental/Picture-in-Cloud|Pictures-in-Clouds]]."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 33, attack +25 - __Cantrips (6th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Figment|Figment]] - __4th__ [[srd/pf2e/compendium/spells/rank-2/Darkness|Darkness]] - __5th__ [[srd/pf2e/compendium/spells/rank-5/Subconscious Suggestion|Subconscious Suggestion]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/Never Mind|Never Mind]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
sourcebook: "_Monster Core 2_, page 97."
```

```encounter-table
name: Destiny Tempest
creatures:
  - 1: Destiny Tempest
```
