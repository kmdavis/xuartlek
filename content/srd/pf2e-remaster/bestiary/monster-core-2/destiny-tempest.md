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
languages: "Sussuran; (can't speak any language); telepathy 100 feet, _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +25, Athletics +21, Deception +26, Dimension of Time Lore +25, Stealth +27"
abilityMods: [4, 8, 6, 8, 7, 7]
ac: 34
armorclass:
  - name: "AC"
    desc: "34; __Fort__: +19; __Ref__: +24; __Will__: +26"
hp: 230
health:
  - name: "HP"
    desc: "230; __Immunities__ bleed, paralyzed, poison, sleep; __Weaknesses__ force 10, spirit 10"
abilities_mid:
  - name: "Ebbing Cloud"
    desc: "(aura, mental, occult) 15 feet. Destiny tempests surround themselves with thoughts of averted fates, creating a thick metaphysical soup that cloys the mind and clouds ambition. Creatures in the area moving toward the destiny tempest treat the area as difficult terrain."
  - name: "No Breath"
    desc: "Destiny tempests do not need to breathe."
  - name: "Unspeakable Insights"
    desc: "(mental, occult) Touching a destiny tempest's mind even briefly grants a powerful and painful awareness of uncharted pasts, presents, and futures, too impossibly vast for mortal minds to conceptualize or contain. Whenever a creature targets the destiny tempest with a magical mental effect, it must attempt a DC 33 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected and becomes immune to unspeakable insights for 24 hours."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature takes 3d6 mental damage."
  - name: "Critical Failure"
    desc: "The creature takes 6d6 mental damage and becomes confused for 1 round."
  - name: "Center of Destiny"
    desc: "⬲ (teleportation)"
  - name: "Trigger"
    desc: "A creature within 30 feet benefits from a fortune effect"
  - name: "Effect"
    desc: "Shadows surround and steal away the destiny tempest, who reappears in an open space adjacent to the triggering creature."
speed: "25 feet, fly 60 feet; swiftness"
attacks:
  - name: "Melee"
    desc: "⬻ slithering whisper +25 (Air, Finesse, Magical) __Damage__ 2d8+10 bludgeoning plus 1d8 mental and sound without voice"
  - name: "Ranged"
    desc: "⬻ umbral breath +25 (Air, range increment 30 feet, Void) __Damage__ 4d10 void"
abilities_bot:
  - name: "Divergent Potential"
    desc: "⬺ (Concentrate, Fortune) The destiny tempest chooses two creatures it can see within 60 feet and rolls two slithering whisper Strikes, one against each creature. After seeing the outcomes of the two Strikes, the destiny tempest chooses one of the two targets to pursue, Flies up to 60 feet to reach the chosen target, and uses the result of the chosen Strike; the other Strike is lost. If the destiny tempest is prevented from reaching its chosen target, the attack is prevented and the chosen Strike is lost."
  - name: "Sound Without Voice"
    desc: "(Air, Emotion, Fear, Mental, Occult) A creature damaged by the destiny tempest's slithering whisper Strike must succeed at a DC 33 basic Will save or become frightened 2."
  - name: "Swiftness"
    desc: "A destiny tempest's movement doesn't trigger reactions. Hushed Voices On the Plane of Air, many creatures communicate through telepathy, shared dreams, or illusory rebuses. Though destiny tempests are telepathic and can magically understand most languages, they prefer to convey their thoughts and ideas metaphorically by shaping the clouds and currents of the Plane of Air to act out elaborate, moving stories and plays. Sometimes these animated clouds retain a bit of magic, becoming Pictures-in-Clouds."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 33, attack +25 - __Cantrips (6th)__ Detect Magic, Figment - __4th__ Darkness - __5th__ Subconscious Suggestion - __6th__ Never Mind - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core 2_, page 97."
```

```encounter-table
name: Destiny Tempest
creatures:
  - 1: Destiny Tempest
```
