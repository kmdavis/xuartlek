---
noteType: pf2eMonster
aliases: "Green Man"
tags:
  - pf2e/creature/level/24
  - pf2e/creature/trait/leshy
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/medium
statblock: inline
name: "Green Man"
level: 24
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4421"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Green Man"
level: "Creature 24"
size: "Medium"
trait_01: "Leshy"
trait_02: "Plant"
trait_03: "Rare"
modifier: 42
perception:
  - name: "Perception"
    desc: "+42; darkvision, plantsense 60 feet"
languages: "Arboreal, [[srd/pf2e/compendium/rules-elements/Languages#Fey|Fey]], [[srd/pf2e/compendium/rules-elements/Languages#Wildsong|Wildsong]]; green tongue"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +39, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +40, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +40, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +40, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +40, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +48, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +41, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +44"
abilityMods: [12, 9, 11, 7, 10, 8]
abilities_top:
  - name: "Green Tongue"
    desc: "A green man can communicate with plants, with the effects of [[srd/pf2e/compendium/spells/rank-3/Speak with Plants|_speak with plants_]], and can use [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] to [[srd/pf2e/compendium/rules-elements/actions/player-core#Make an Impression|Make an Impression]] on plants and [[srd/pf2e/compendium/rules-elements/actions/player-core#Request|Request]] things from plants."
  - name: "Plantsense"
    desc: "A green man can sense life force via plants. This allows them to observe a living or undead creature's vital essence within 60 feet of the green man, but they can also use this precise sense to observe any living or undead creature within 60 feet of any plant matter within 120 feet of the green man. This allows the green man to see living things through solid plant matter, as well as seeing through other barriers if there are plants on the other side."
ac: 51
armorclass:
  - name: "AC"
    desc: "51; __Fort__: +43; __Ref__: +39; __Will__: +42"
hp: 525
health:
  - name: "HP"
    desc: "525; __Resistances__ bludgeoning 20, piercing 20; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/Weapon Groups#Axe|axes]] 20, fire 20"
abilities_mid:
  - name: "Green Caress"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Plant|plant]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|primal]]) 60 feet. Living creatures in the area other than plants slowly transform into non-creature plants. The green man can exclude creatures from this effect, but they must be aware of a creature's presence and location to do so. A non-plant creature in the area must attempt a DC 45 Fortitude save immediately before the start of its turn."
  - name: "Critical Success"
    desc: "The creature is unaffected, or if it is slowed by green caress, it reduces its slowed value by 2."
  - name: "Success"
    desc: "The creature is unaffected, or if it is [[srd/pf2e/compendium/rules-elements/Conditions#Slowed|slowed]] by green caress, it reduces its slowed value by 1."
  - name: "Failure"
    desc: "The creature becomes slowed 1, or if it was already slowed by green caress, increases the slowed value by 1, as their body transforms more and more into a non-creature plant. If the creature ever becomes slowed to the point they have no actions left for their turn, they become an inanimate plant, a condition that can only be reversed by [[srd/pf2e/compendium/spells/rank-10/Manifestation|_manifestation_]] or similarly powerful magic."
  - name: "Critical Failure"
    desc: "As failure, except the creature becomes slowed 2 (or increases the condition value by 2)."
  - name: "Root In Place"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within the green man's reach uses a [[srd/pf2e/compendium/rules-elements/traits/player-core/Move|move]] action or leaves a square during a move action it's using"
  - name: "Effect"
    desc: "The green man lashes out to hold the foe in place. The green man makes a vine Strike against the triggering creature. If the attack hits, the green man disrupts the action. If the creature was [[srd/pf2e/books/npc-core/creature-companions/Pets and Familiars#Flying|Flying]] when its action was disrupted, it falls."
speed: "40 feet, climb 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ vine +46 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly 3d12]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 30 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile P]]) __Damage__ 4d10+27 bludgeoning plus Absorb Magic and Improved Grab"
  - name: "Ranged"
    desc: "⬻ thorn +43 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Fatal|fatal d12]], range increment 120 feet, reload 0) __Damage__ 4d8+27 piercing plus embed"
abilities_bot:
  - name: "Absorb Magic"
    desc: "⬻ The green man's vines leach away magic and transform it into life essence for the green man. On a successful vine Strike, the green man attempts to [[srd/pf2e/books/player-core/chapter-7-spells/Counteracting|counteract]] one spell active on the target (typically one vexing the green man, or determined randomly if they aren't aware of specific effects), with a counteract rank of 10 and a modifier of +38. If the effect is counteracted, the green man gains 30 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Hit Points, Healing, and Dying#Temporary Hit Points|temporary Hit Points]] that last for 10 minutes."
  - name: "Embed"
    desc: "The green man's thorns embed themselves into any creature they damage, taking root into the ground. A target damaged by a thorn has its Speeds halved, and it can't [[srd/pf2e/compendium/rules-elements/actions/player-core#Step|Step]], [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Fly]], or otherwise leave the ground until the thorn is removed. Removing a thorn requires 3 [[srd/pf2e/compendium/rules-elements/actions/player-core#Interact|Interact]] actions, which don't have to be consecutive. If the creature performing the final action doesn't succeed at a DC 45 [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] check as part of that action, the target takes 10d6 piercing damage upon the thorn's removal."
  - name: "Focus Vines"
    desc: "⬺ The green man focuses all their vines against a single vexing foe, making a single vine Strike. On a success, the target takes 5d10 additional bludgeoning damage and is affected by Absorb Magic three times. Even on a failure, the target takes the normal effects of a hit with a vine Strike, but on a critical failure, the vines miss completely."
  - name: "Green Grab"
    desc: "A green man can use their Improved Grab action against a creature of any size."
  - name: "Green Rituals"
    desc: "A green man can perform all their rituals without secondary casters, relying on their own primal ties to the vital essence in spirits of nature. A green man's [[srd/pf2e/compendium/spells/rituals/Awaken Animal|awaken animal]] and [[srd/pf2e/compendium/spells/rituals/Primal Call|primal call]] rituals work on plants instead of their usual range of choices. Most green men also know the ritual to create various types of [[srd/pf2e/compendium/gm/creature-families/Leshy|leshies]] and possibly even magic allowing the creation of [[srd/pf2e/compendium/gm/creature-families/Arboreal|arboreals]] or more powerful [[srd/pf2e/compendium/rules-elements/traits/player-core/Plant|plant]] creatures."
  - name: "Vine Forest"
    desc: "⬺ The green man lashes out with all six vines to attack many opponents. They make up to six vine Strikes, each against a different target; this counts as one attack for their multiple attack penalty, increasing only after all the attacks are made. Leshies And Green Men Green men are sometimes called “[[srd/pf2e/compendium/gm/creature-families/Leshy|leshy]] kings” in ancient manuscripts. [[srd/pf2e/compendium/character/classes/Druid|Druids]] consider the first green men to be the original source of the rituals for creating the less-deific leshies, and possibly even [[srd/pf2e/compendium/gm/creature-families/Arboreal|arboreals]] and other intelligent plants. The affinity between leshies and green men is mutual. Leshies are the most likely ancestry to worship green men, and green men are particularly fond of their less-powerful kin. Worshipping Green Men Individual [[srd/pf2e/compendium/deities/green-man-faiths/Green Man|green men]] are lesser deities, capable of granting spells to those who worship them. Green men typically only allow intelligent plants—such as [[srd/pf2e/compendium/gm/creature-families/Leshy|leshies]]—to be their [[srd/pf2e/compendium/character/classes/Cleric|clerics]]. If another creature proves to be a friend of plants, after a thorough personal vetting, a green man might wholeheartedly accept this strange fleshy worshipper into the fold. While individual green men have different edicts and anathema befitting their personalities, the following is a baseline most worshippers of green men follow."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 48 - __Cantrips (10th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Read Aura|Read Aura]] - __8th__ [[srd/pf2e/compendium/spells/rank-4/Fly|Fly]], [[srd/pf2e/compendium/spells/rank-4/Unfettered Movement|Unfettered Movement]] - __9th__ [[srd/pf2e/compendium/spells/rank-7/Energy Aegis|Energy Aegis]] - __10th__ [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]] (×3), [[srd/pf2e/compendium/spells/rank-10/Manifestation|Manifestation]] (×3), [[srd/pf2e/compendium/spells/rank-5/Nature's Pathway|Nature's Pathway]] (at will), [[srd/pf2e/compendium/spells/rank-7/Regenerate|Regenerate]] (×3), [[srd/pf2e/compendium/spells/rank-6/Truesight|Truesight]]"
  - name: "Rituals"
    desc: "DC 48 - __4th__ [[srd/pf2e/compendium/spells/rituals/Plant Growth|Plant Growth]] - __6th__ [[srd/pf2e/compendium/spells/rituals/Awaken Animal|Awaken Animal]], [[srd/pf2e/compendium/spells/rituals/Commune|Commune]], [[srd/pf2e/compendium/spells/rituals/Primal Call|Primal Call]] - __8th__ [[srd/pf2e/compendium/spells/rituals/Control Weather|Control Weather]]"
sourcebook: "_Monster Core 2_, page 174."
```

```encounter-table
name: Green Man
creatures:
  - 1: Green Man
```
