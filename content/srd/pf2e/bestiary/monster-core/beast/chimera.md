---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Chimera"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Chimera"
level: 8
source: "Monster Core"
aon_id: "creature-2879"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2879"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Chimera"
level: "Creature 8"
size: "Large"
trait_01: "Beast"
trait_02: "Uncommon"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +14, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +18, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +18"
abilityMods: [6, 2, 4, -3, 2, 0]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +18; __Ref__: +16; __Will__: +14"
hp: 135
health:
  - name: "HP"
    desc: "135"
abilities_mid:
  - name: "Multiple Reactions"
    desc: "A chimera gains 2 extra reactions each round that it can use only to make Reactive Strikes. It must use a different head for each reaction, and it can't use more than one on the same triggering action. If it loses one of its heads, it also loses one of these extra reactions."
  - name: "Three Headed"
    desc: "Any ability that would sever a chimera's head (such as a critical hit with a [[srd/pf2e/compendium/equipment/runes/vorpal|_vorpal_]] weapon) severs one head at random. Losing a head doesn't kill a chimera (as long as it has one head left), but it does prevent it from making Strikes with the lost head or using the head's Dragon Breath."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dragon jaws +20 __Damage__ 2d6+9 piercing plus 2d6 energy damage (see draconic bite)"
  - name: "Melee"
    desc: "⬻ lion jaws +20 __Damage__ 2d10+9 piercing"
  - name: "Melee"
    desc: "⬻ goat horns +20 __Damage__ 2d10+9 piercing"
  - name: "Melee"
    desc: "⬻ claw +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d6+9 slashing"
abilities_bot:
  - name: "Draconic Bite"
    desc: "A chimera's dragon head deals an extra 2d6 damage of a type matching the damage dealt by its Dragon Breath."
  - name: "Dragon Breath"
    desc: "⬺ The chimera breathes a cone or line that deals 9d6 damage to all creatures in the area (DC 26 basic save of a type indicated below). The chimera's dragon head is linked to one of the traditions of magic, which determines the area of its Dragon Breath, the type of damage it deals, and the type of save to avoid it. This ability gains the related traits. The chimera can't use Dragon Breath again for 1d4 rounds. Arcane 60-foot line of [[srd/pf2e/compendium/rules-elements/traits/player-core/force|force]] (Reflex)Divine 60-foot line of [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]] (Reflex); this ability can also have the [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]] traitOccult 30-foot cone of [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]] (Will)Primal 30-foot cone of [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]], [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]], [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/sonic|sonic]] (Reflex); or [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]] (Fortitude)"
  - name: "Three-Headed Strike"
    desc: "⬺ The chimera makes a Strike with its dragon jaws, lion jaws, and goat horns, each at a –2 penalty and targeting a different creature. These Strikes count as only one attack for the chimera's multiple attack penalty, and the penalty doesn't increase until after it has made all three attacks. Kobold Adoration Some [[srd/pf2e/compendium/gm/creature-families/kobold|kobold]] groups are fond of chimera guardians or pets, but few kobolds have the bravery or resources to keep a chimera happy for long. Chimeras are voracious eaters, and while a family of kobolds might appreciate having one as a guardian, they can instead find it more dangerous than the threats they'd hoped it would protect them from if they can't keep it fed."
sourcebook: "_Monster Core_, page 62."
```

```encounter-table
name: Chimera
creatures:
  - 1: Chimera
```
