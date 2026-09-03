---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Balisse"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/angel
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/medium
statblock: inline
name: "Balisse"
level: 8
source: "Monster Core"
aon_id: "creature-2816"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2816"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Balisse"
level: "Creature 8"
size: "Medium"
trait_01: "Angel"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; (20 to detect lies and [[srd/pf2e/compendium/rules-elements/traits/player-core/illusion|illusions]]) darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]]; [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +14, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +17, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +18"
abilityMods: [5, 2, 4, 1, 6, 5]
abilities_top:
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/sword/scimitar|scimitar]]_"
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +16; __Ref__: +12; __Will__: +18 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 145
health:
  - name: "HP"
    desc: "145; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 15; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]] 10 Confessor's Aura (aura, divine, mental) 20 feet. Creatures in the balisse's aura are subject to [[srd/pf2e/compendium/spells/rank-3/ring-of-truth|_ring of truth_]] (DC 23). Additionally, if these creatures choose to honestly express their own conflicted feelings, the aura makes it easier for them to put words to those feelings."
speed: "30 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ scimitar +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/forceful|Forceful]], [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 2d6+8 slashing plus 1d6 fire"
abilities_bot:
  - name: "Brand of the Impenitent"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The balisse marks a creature within their confessor's aura as irredeemable. They can do so only after a failed attempt to convince the creature to repent. The touched creature takes a –1 status penalty to AC and saves, reduces all its resistances by 2, and gains weakness 2 to [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]]. The duration depends on the target's DC 26 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The duration is 1 round."
  - name: "Failure"
    desc: "The duration is 1 day."
  - name: "Critical Failure"
    desc: "The duration is unlimited."
  - name: "Guiding Angel"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]])"
  - name: "Requirements"
    desc: "The balisse is [[srd/pf2e/compendium/rules-elements/conditions#Invisible|invisible]]"
  - name: "Effect"
    desc: "The balisse spiritually attaches themself to an adjacent mortal who doesn't have the [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]] trait. They merge with the mortal's body and are unable to use any of their spells and abilities other than to interact with the mortal. They can Dismiss the effect to leave the mortal. While merged, the balisse can either communicate using a bodiless voice only the mortal can hear or can take a form of their choice that only the mortal can see, such as a small angel on the mortal's shoulder."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 26 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/invisibility|Invisibility]] (at will; self only) - __3rd__ [[srd/pf2e/compendium/spells/rank-2/clear-mind|Clear Mind]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-2/cleanse-affliction|Cleanse Affliction]], [[srd/pf2e/compendium/spells/rank-4/divine-wrath|Divine Wrath]], [[srd/pf2e/compendium/spells/rank-1/heal|Heal]], [[srd/pf2e/compendium/spells/rank-3/paralyze|Paralyze]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]]"
  - name: "Rituals"
    desc: "DC 26 - __1st__ [[srd/pf2e/compendium/spells/rituals/angelic-messenger|Angelic Messenger]] - __3rd__ Geas - __4th__ Atone"
sourcebook: "_Monster Core_, page 15."
```

```encounter-table
name: Balisse
creatures:
  - 1: Balisse
```
