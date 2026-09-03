---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Anemos"
tags:
  - pf2e/creature/level/18
  - pf2e/creature/trait/air
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/medium
statblock: inline
name: "Anemos"
level: 18
source: "Rage of Elements"
aon_id: "creature-2614"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2614"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Anemos"
level: "Creature 18"
size: "Medium"
trait_01: "Air"
trait_02: "Elemental"
trait_03: "Rare"
modifier: 33
perception:
  - name: "Perception"
    desc: "Perception +33; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]], [[srd/pf2e/compendium/rules-elements/languages#Sussuran|Sussuran]]; truespeech"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +38, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +31, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +33, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +31, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +38, Planar Lore +33, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +31, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +36, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +33"
abilityMods: [4, 9, 7, 6, 6, 9]
abilities_top:
  - name: "Truespeech"
    desc: "An anemos can speak with and understand any creature that has a language."
  - name: "Wind Orchestra"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/air|air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|auditory]]) An anemos does not require instruments to perform music, instead using their winds to create and carry the sounds of any instruments they wish to duplicate. They can mimic any number of instruments simultaneously, creating and directing their own personal orchestra."
ac: 43
armorclass:
  - name: "AC"
    desc: "43; __Fort__: +29; __Ref__: +33; __Will__: +30"
hp: 310
health:
  - name: "HP"
    desc: "310 , regeneration 15 (deactivated by earthbane); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 20"
abilities_mid:
  - name: "Blessed by the Winds"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/air|air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]]) 80 feet. The winds grow turbulent for those who would dare to fly in the same space as an anemos, but they take care to never harm or inconvenience their shepherd. Air within the emanation is difficult terrain for Flying creatures that do not have the [[srd/pf2e/compendium/rules-elements/traits/player-core/air|air]] trait. While the aura is active, the anemos cannot be affected by environmental air or weather affects unless they choose to be."
  - name: "Earthbane"
    desc: "An anemos's regeneration is suppressed for 1 round if the anemos is affected by an [[srd/pf2e/compendium/rules-elements/traits/player-core/earth|earth]] effect, or for as long as they are in contact with the ground and 1 round thereafter. If an anemos is submerged in at least 1 inch of mud, dirt, or stone, the anemos's aura deactivates, and the anemos becomes stunned 2 and clumsy 2."
  - name: "Redirect Weather"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]])"
  - name: "Requirements"
    desc: "The anemos's aura is active"
  - name: "Trigger"
    desc: "A creature within the anemos's aura uses an [[srd/pf2e/compendium/rules-elements/traits/player-core/air|air]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] spell, or an air or electricity spell otherwise comes into effect within the anemos's aura"
  - name: "Effect"
    desc: "The winds and weather of the spell obey the anemos's call. The anemos makes all the choices to determine the targets, destination, or other effects of the spell, as though they were the caster."
speed: "25 feet, fly 200 feet; swiftness"
attacks:
  - name: "Melee"
    desc: "⬻ thunderbolt +35 ([[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|Electricity]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 3d8+12 electricity plus 3d6 sonic"
  - name: "Ranged"
    desc: "⬻ air blast +35 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/air|Air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range 100 feet) __Damage__ 3d10+12 bludgeoning"
  - name: "Ranged"
    desc: "⬻ thunderbolt +35 ([[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|Electricity]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 30 feet]]) __Damage__ 3d8+10 electricity plus 3d6 sonic"
abilities_bot:
  - name: "Divine Rituals"
    desc: "DC 40 - __6th__ [[srd/pf2e/compendium/spells/rituals/sky-signs|Sky Signs]] - __8th__ Control Weather"
  - name: "Collect Thunder"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|Electricity]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]])"
  - name: "Requirements"
    desc: "The anemos has a hand free"
  - name: "Effect"
    desc: "The anemos runs a hand through the winds that swirl around them, the sparks from their fingertips coalescing into a thunderbolt. The anemos creates a thunderbolt in their open hand. If the anemos spends an action to Collect Thunder, a bolt instead strikes their open hand, creating a booming peal that deafens all creatures within 20 feet for 1 round unless they succeed at a DC 40 Fortitude save; this adds the [[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|auditory]] trait to Collect Thunder. Any thunderbolts dissipate after 1 round."
  - name: "Command the Breeze"
    desc: "When an anemos casts a ritual, they perform all aspects of the ritual themself, commanding their winds to complete all the ritual's components. They must fulfill any requirements for the ritual's additional casters and must attempt the checks normally performed by additional casters. In addition, anemoi can cast rituals faster than usual. If a ritual has a casting time measured in days, they can cast it in an equal number of hours."
  - name: "Storm Strikes Twice"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/air|Air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|Teleportation]]) The anemos throws a thunderbolt, then becomes a wind that carries them in an instant to the bolt's location to attack again. They make a ranged thunderbolt Strike against a creature within their first range increment, teleport to the creature's location as a gust of wind, then grasp the thrown thunderbolt and make a melee thunderbolt Strike against a creature within reach. Their multiple attack penalty doesn't increase until they've made both attacks."
  - name: "Swiftness"
    desc: "The anemos's movement doesn't trigger reactions. The Cardinal Anemoi Anemoi who are particularly ancient and powerful often have their own unique capabilities. In addition to their standard abilities, Golarion's cardinal anemoi possess the following additional innate spells."
  - name: "Austral"
    desc: "the south wind: __8th__ _flame vortex_; __5th__ _geyser_"
  - name: "Boreal"
    desc: "the north wind: __8th__ _frigid flurry_; __5th__ _howling blizzard_"
  - name: "Eural"
    desc: "the east wind: __8th__ _chain lightning_; __5th__ [[srd/pf2e/compendium/spells/rank-5/pressure-zone|_pressure zone_]]"
  - name: "Zephyr"
    desc: "the west wind: __8th__ _field of life_; __4th__ _petal storm_, _speak with plants_ The Shape of the Air Anemoi on the [[srd/pf2e/compendium/gm/planes#Plane of Air|Plane of Air]] are typically genderless, while those who spend time in the Universe sometimes experiment with or develop preferences for one of the genders of the mortals they watch or live close to."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 40 - __1st__ [[srd/pf2e/compendium/spells/rank-1/air-bubble|Air Bubble]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-4/airlift|Airlift]] (at will), [[srd/pf2e/compendium/spells/rank-4/vapor-form|Vapor Form]] (at will), [[srd/pf2e/compendium/spells/rank-2/voice-on-the-breeze|Voice on the Breeze]] (at will) - __7th__ [[srd/pf2e/compendium/spells/rank-2/humanoid-form|Humanoid Form]] (at will) - __9th__ [[srd/pf2e/compendium/spells/rank-2/cleanse-air|Cleanse Air]]"
sourcebook: "_Rage of Elements_, page 78."
```

```encounter-table
name: Anemos
creatures:
  - 1: Anemos
```
