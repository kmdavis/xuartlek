---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Kodama"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/kami
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/small
statblock: inline
name: "Kodama"
level: 5
source: "Monster Core 2"
aon_id: "creature-4454"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4454"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Kodama"
level: "Creature 5"
size: "Small"
trait_01: "Kami"
trait_02: "Spirit"
trait_03: "Wood"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]]; speak with plants, telepathy 50 feet (page 362)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +11, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +11, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +13, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +13, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +13"
abilityMods: [2, 4, 5, 0, 4, 4]
abilities_top:
  - name: "Ward"
    desc: "(divine) Every kami is bound to a ward: a specific animal, plant, object, or location. A kami can merge with or emerge from their ward as a single action, which has the concentrate trait. While merged, the kami can observe their surroundings with their usual senses as well as the senses of their ward, but can't move, communicate with, or control their ward. Additionally, a kami merged with their ward recovers Hit Points each minute as if they spent an entire day resting. A kodama's ward is typically a specific tree."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/adventuring-gear/rope|spiritual rope]]"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +12; __Ref__: +11; __Will__: +13 +1 status to AC and all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]] effects and attacks and effects from unholy creatures"
hp: 95
health:
  - name: "HP"
    desc: "95; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]] 5; __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/cold-iron-object-high-grade|cold iron]] 5 Distracting Gaze (aura, divine, visual) 30 feet. When a creature ends its turn in the aura, it must attempt a DC 21 Will save. The kodama can activate or deactivate this aura by using a single action, which has the [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]] trait."
abilities_mid:
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]] with the kodama. This condition ends if the creature ends its turn outside the aura."
  - name: "Critical Failure"
    desc: "As failure, plus the creature is [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] 1 as long as it remains fascinated."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]]) __Damage__ 2d6+4 bludgeoning"
abilities_bot:
  - name: "Innate Divine Spells"
    desc: "DC 23 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/figment|Figment]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/one-with-plants|One with Plants]] - __5th__ [[srd/pf2e/compendium/spells/rank-5/natures-pathway|Nature's Pathway]] - __Constant (4th)__ [[srd/pf2e/compendium/spells/rank-3/speak-with-plants|Speak with Plants]]"
  - name: "Spiritual Rope"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]]) The kodama spends 1 minute to fashion an enchanted straw rope out of nearby materials. The rope can be wrapped around other kami creatures to protect them from fell forces. A kami who wears a _spiritual rope_ gains resistance 5 to damage from unholy creatures and effects and a +1 status bonus to AC and saving throws against [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]] effects and attacks and effects from unholy creatures. A kodama always wears a spiritual rope, and they can have one other spiritual rope in existence at a time. Creating a new rope beyond these two releases the magic of one of the other two ropes of the kodama's choosing. A spiritual rope around a creature other than a kodama loses its magic after 24 hours or if it's taken outside the kodama's forest. Kami Treasure Kami have no use for valuables or other material possessions, but the sites they protect are often rich with natural resources or even sometimes dotted with relics from bygone eras. One of the greatest kami treasures is a kodama’s _spiritual rope_. Although these ropes grant no power to mortals, a freely gifted _spiritual rope_ from a kodama is seen as a mark of the utmost purity and worthiness."
sourcebook: "_Monster Core 2_, page 205."
```

```encounter-table
name: Kodama
creatures:
  - 1: Kodama
```
