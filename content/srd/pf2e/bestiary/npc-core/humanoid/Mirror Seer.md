---
noteType: pf2eMonster
aliases: "Mirror Seer"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/medium
statblock: inline
name: "Mirror Seer"
level: 9
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3541"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Mirror Seer"
level: "Creature 9"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Rare"
modifier: 16
perception:
  - name: "Perception"
    desc: "+16"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Fey|Fey]], [[srd/pf2e/compendium/rules-elements/Languages#Shadowtongue|Shadowtongue]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +21, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +17, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +19, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +17, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +17, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +17"
abilityMods: [2, 2, -1, 4, 3, 5]
abilities_top:
  - name: "Looking Glass Magic"
    desc: "The mirror seer accesses power from their wicked benefactor through two mirrors: one full-sized [[srd/pf2e/compendium/equipment/other/Malefic Mirror|_malefic mirror_]] in their sanctum and an _enchanted hand mirror_ they can carry on their person."
  - name: "Malefic Mirror"
    desc: "The mirror seer must visit the _malefic mirror_ once per day to retain their spellcasting abilities, and they can activate the mirror for special [[srd/pf2e/compendium/spells/rank-6/Scrying|_scrying_]] and [[srd/pf2e/compendium/spells/rank-1/Illusory Disguise|_illusory disguise_]] spells as noted in the mirror's stat block."
  - name: "Enchanted Hand Mirror"
    desc: "Without their enchanted hand mirror on their person, the mirror seer takes a –2 circumstance penalty to spell attack rolls and DCs and can't cast their 7th-rank spells. If it's not attended by the mirror seer, the hand mirror has AC 10, Hardness 0, and 1 HP."
  - name: "Items"
    desc: "_+1 dagger_, _enchanted hand mirror_, [[srd/pf2e/compendium/spells/rank-5/False Vision|_scroll of false vision_]], _+1 [[srd/pf2e/compendium/equipment/runes/Striking|striking]] [[srd/pf2e/compendium/equipment/weapons/club/Staff|staff]]_"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +14; __Ref__: +17; __Will__: +20"
hp: 140
health:
  - name: "HP"
    desc: "140"
abilities_mid:
  - name: "Rightfully Mine"
    desc: "⬲"
  - name: "Trigger"
    desc: "The mirror seer observes a creature making a Strike, casting a spell of 4th rank or lower, or using a special action (the triggering action must take 2 actions or fewer); Effect The mirror seer expends a 4th-rank spell slot (or higher) to duplicate the triggering action. This mimicked action occurs immediately after the triggering action, using the triggering creature's statistics unless the mirror seer's are higher. The creature the mirror seer mimicked is then temporarily immune to this ability for 10 minutes."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _staff_ +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Two-Hand|two-hand d8]]) __Damage__ 2d4+8 bludgeoning"
  - name: "Melee"
    desc: "⬻ dagger +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+8 piercing"
  - name: "Melee"
    desc: "⬻ fist +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+8 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+8 piercing"
abilities_bot:
  - name: "A Fairer Face"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]]) The mirror seer chooses a creature within 100 feet that can see its own reflection in a mirror. The creature must succeed at a DC 29 Will save or become [[srd/pf2e/compendium/rules-elements/Conditions#Fascinated|fascinated]] by their reflection for 1 minute. The creature can attempt a new save to end the effect at the end of each of its turns."
  - name: "Hall of Mirrors"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Illusion|Illusion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Manipulate|Manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The mirror seer causes all surfaces in a 30-foot burst within 100 feet to become reflective for 1 minute. Every creature in the area or that later enters the area must succeed at a DC 27 Will save or become [[srd/pf2e/compendium/rules-elements/Conditions#Confused|confused]] by the reflections and refractions. The confusion ends if the creature leaves the area, and the creature can attempt a new save to end the effect at the end of each of its turns. When the effect ends for a creature, that creature becomes temporarily immune for 10 minutes. The Mirror Gazes Back The mirror seer's great power stems from their [[srd/pf2e/compendium/equipment/other/Malefic Mirror|_malefic mirror_]]. The story of the being and power behind the mirror can be told in many ways. Is it a [[srd/pf2e/compendium/gm/creature-families/Demon|demon]] trapped in the confines of the item, loathing its prison and yearning to be released? An entity working its will in our world through the mirror seer? Both of these have been true of mirror seers in history. And those who defeat a mirror seer might find themselves speaking to the mirror. Or even making their own pact, secure that they, surely, can avoid being corrupted..."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 29, attack +21 - __Cantrips (5th)__ [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/Figment|Figment]], [[srd/pf2e/compendium/spells/cantrips/Prestidigitation|Prestidigitation]], [[srd/pf2e/compendium/spells/cantrips/Telekinetic Projectile|Telekinetic Projectile]], [[srd/pf2e/compendium/spells/cantrips/Void Warp|Void Warp]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Alarm|Alarm]], [[srd/pf2e/compendium/spells/rank-1/Fear|Fear]], [[srd/pf2e/compendium/spells/rank-1/Item Facade|Item Facade]] (3 slots) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]], [[srd/pf2e/compendium/spells/rank-2/Revealing Light|Revealing Light]], [[srd/pf2e/compendium/spells/rank-2/Status|Status]] (3 slots) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Clairaudience|Clairaudience]], [[srd/pf2e/compendium/spells/rank-3/Hypnotize|Hypnotize]], [[srd/pf2e/compendium/spells/rank-3/Locate|Locate]] (3 slots) - __4th__ [[srd/pf2e/compendium/spells/rank-4/Clairvoyance|Clairvoyance]], [[srd/pf2e/compendium/spells/rank-4/Detect Scrying|Detect Scrying]], [[srd/pf2e/compendium/spells/rank-4/Peaceful Bubble|Peaceful Bubble]] (3 slots) - __5th__ [[srd/pf2e/compendium/spells/rank-5/Illusory Scene|Illusory Scene]], [[srd/pf2e/compendium/spells/rank-5/Shadow Blast|Shadow Blast]] (2 slots) - __7th__ [[srd/pf2e/compendium/spells/rank-1/Illusory Disguise|Illusory Disguise]] (self only), [[srd/pf2e/compendium/spells/rank-6/Scrying|Scrying]] (2 slots)"
sourcebook: "_NPC Core_, page 101."
```

```encounter-table
name: Mirror Seer
creatures:
  - 1: Mirror Seer
```
