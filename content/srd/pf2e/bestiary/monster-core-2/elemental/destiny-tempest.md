---
obsidianUIMode: preview
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
aon_id: "creature-4324"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4324"
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
    desc: "Perception +26; greater darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Sussuran|Sussuran]]; (can't speak any language); telepathy 100 feet, [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +25, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +21, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +26, [[srd/pf2e/compendium/rules-elements/skills/lore|Dimension of Time Lore]] +25, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +27"
abilityMods: [4, 8, 6, 8, 7, 7]
ac: 34
armorclass:
  - name: "AC"
    desc: "34; __Fort__: +19; __Ref__: +24; __Will__: +26"
hp: 230
health:
  - name: "HP"
    desc: "230; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/force|force]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]] 10"
abilities_mid:
  - name: "Ebbing Cloud"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]) 15 feet. Destiny tempests surround themselves with thoughts of averted fates, creating a thick metaphysical soup that cloys the mind and clouds ambition. Creatures in the area moving toward the destiny tempest treat the area as difficult terrain."
  - name: "No Breath"
    desc: "Destiny tempests do not need to breathe."
  - name: "Unspeakable Insights"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]) Touching a destiny tempest's mind even briefly grants a powerful and painful awareness of uncharted pasts, presents, and futures, too impossibly vast for mortal minds to conceptualize or contain. Whenever a creature targets the destiny tempest with a magical mental effect, it must attempt a DC 33 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected and becomes immune to unspeakable insights for 24 hours."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature takes 3d6 mental damage."
  - name: "Critical Failure"
    desc: "The creature takes 6d6 mental damage and becomes [[srd/pf2e/compendium/rules-elements/conditions#Confused|confused]] for 1 round."
  - name: "Center of Destiny"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|teleportation]])"
  - name: "Trigger"
    desc: "A creature within 30 feet benefits from a [[srd/pf2e/compendium/rules-elements/traits/player-core/fortune|fortune]] effect"
  - name: "Effect"
    desc: "Shadows surround and steal away the destiny tempest, who reappears in an open space adjacent to the triggering creature."
speed: "25 feet, fly 60 feet; swiftness"
attacks:
  - name: "Melee"
    desc: "⬻ slithering whisper +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/air|Air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 2d8+10 bludgeoning plus 1d8 mental and sound without voice"
  - name: "Ranged"
    desc: "⬻ umbral breath +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/air|Air]], range increment 30 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/void|Void]]) __Damage__ 4d10 void"
abilities_bot:
  - name: "Divergent Potential"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fortune|Fortune]]) The destiny tempest chooses two creatures it can see within 60 feet and rolls two slithering whisper Strikes, one against each creature. After seeing the outcomes of the two Strikes, the destiny tempest chooses one of the two targets to pursue, [[srd/pf2e/books/player-core/chapter-8-playing-the-game/immunity-weakness-and-resistance|Flies]] up to 60 feet to reach the chosen target, and uses the result of the chosen Strike; the other Strike is lost. If the destiny tempest is prevented from reaching its chosen target, the attack is prevented and the chosen Strike is lost."
  - name: "Sound Without Voice"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/air|Air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) A creature damaged by the destiny tempest's slithering whisper Strike must succeed at a DC 33 basic Will save or become [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened 2]]."
  - name: "Swiftness"
    desc: "A destiny tempest's movement doesn't trigger reactions. Hushed Voices On the [[srd/pf2e/compendium/gm/planes#Plane of Air|Plane of Air]], many creatures communicate through telepathy, shared dreams, or illusory rebuses. Though destiny tempests are telepathic and can magically understand most languages, they prefer to convey their thoughts and ideas metaphorically by shaping the clouds and currents of the Plane of Air to act out elaborate, moving stories and plays. Sometimes these animated clouds retain a bit of magic, becoming [[srd/pf2e/bestiary/rage-of-elements/elemental/picture-in-cloud|Pictures-in-Clouds]]."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 33, attack +25 - __Cantrips (6th)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/figment|Figment]] - __4th__ [[srd/pf2e/compendium/spells/rank-2/darkness|Darkness]] - __5th__ [[srd/pf2e/compendium/spells/rank-5/subconscious-suggestion|Subconscious Suggestion]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/never-mind|Never Mind]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]]"
sourcebook: "_Monster Core 2_, page 97."
```

```encounter-table
name: Destiny Tempest
creatures:
  - 1: Destiny Tempest
```
