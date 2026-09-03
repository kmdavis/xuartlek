---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Theletos"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/aeon
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/medium
statblock: inline
name: "Theletos"
level: 7
source: "Monster Core 2"
aon_id: "creature-4012"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4012"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Theletos"
level: "Creature 7"
size: "Medium"
trait_01: "Aeon"
trait_02: "Monitor"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; darkvision"
languages: "envisioning"
abilityMods: [4, 4, 3, 3, 5, 3]
abilities_top:
  - name: "Envisioning"
    desc: "When a theletos conveys information, it does so wordlessly through psychic projections. This acts as telepathy with a range of 100 feet but is understandable to all creatures regardless of whether they have a language. The meaning to non-aeons can be vague and is often mysterious. A theletos can use this ability to communicate flawlessly with any other aeon on the same plane."
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +16; __Ref__: +13; __Will__: +18 +1 status to all saves vs. magic"
hp: 125
health:
  - name: "HP"
    desc: "125; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]] 5"
speed: "25 feet, fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 2d10+8 bludgeoning"
  - name: "Melee"
    desc: "⬻ tentacle +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d8+8 slashing plus fate drain"
abilities_bot:
  - name: "Fate Drain"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) A creature damaged by the theletos’s tentacle must succeed at a DC 22 Will save or become [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied]] 1. As long as the creature is stupefied, it can no longer benefit from [[srd/pf2e/compendium/rules-elements/traits/player-core/fortune|fortune]] effects. If the target fails additional saves against this ability, the condition value increases by 1 (to a maximum of stupefied 4). This condition value decreases by 1 every 24 hours."
  - name: "Wrath of Fate"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/misfortune|Misfortune]]) The theletos releases a 60-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Cone|cone]] of energy from its center. Creatures in the cone become overwhelmed with the knowledge of various fates that destiny has in store for them and lack of clear pathways to these potential futures. They must succeed at a DC 26 Will save or be [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] 1 indefinitely. An affected creature can choose to roll twice when it attempts an attack, saving throw, or skill check and take the lower result. Regardless of the outcome, that creature is no longer slowed after that roll. The theletos can’t use Wrath of Fate again for 1d4 rounds. Maintaining the Balance Theletoses care little for the individuals and societies they manipulate, only that the balance between freedom and fate is maintained. A theletos might help a creature who has lost their freedom escape, but they might also force those who swore to perform an unjust duty to stick to their word. If their plans are thwarted, a theletos doesn’t seek revenge but instead looks for other ways to redress the balance."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 25, attack +17 - __4th__ [[srd/pf2e/compendium/spells/rank-2/augury|Augury]] (at will), [[srd/pf2e/compendium/spells/rank-1/charm|Charm]], [[srd/pf2e/compendium/spells/rank-2/cleanse-affliction|Cleanse Affliction]], [[srd/pf2e/compendium/spells/rank-2/dispel-magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-3/enthrall|Enthrall]], [[srd/pf2e/compendium/spells/rank-4/outcasts-curse|Outcast's Curse]], [[srd/pf2e/compendium/spells/rank-4/suggestion|Suggestion]], [[srd/pf2e/compendium/spells/rank-2/stupefy|Stupefy]]"
  - name: "Rituals"
    desc: "DC 25 - __3rd__ [[srd/pf2e/compendium/spells/rituals/geas|Geas]]"
sourcebook: "_Monster Core 2_, page 10."
```

```encounter-table
name: Theletos
creatures:
  - 1: Theletos
```
