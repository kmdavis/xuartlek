---
hp: "28"
ac: "16"
modifier: "4"
level: "2"
player: Levi
class: Alchemist
ancestry: Gnome
source: Foundry export fvtt-Actor-gripp-(levi)-MsQdnK3mmARxEEcK.json
---

```statblock
layout: Basic Pathfinder 2e Layout
name: Gripp
level: 2
ancestry: Gnome # unrendered
heritage: Sensate Gnome # unrendered
background: Barkeep # unrendered
class: Alchemist # unrendered

rare_03: Alchemist # class
rare_04: Barkeep # background
size: Small
trait_01: Gnome
trait_02: Humanoid

modifier: 4 # unrendered
perception:
  - name: Perception
    desc: "Perception +4"
languages:
- Common
- Fey
- Gnomish
skills:
  acrobatics: +5
  crafting: +8
  deception: +7
  diplomacy: +7
  medicine: +4
  nature: +4
  society: +8
  stealth: +5
  survival: +4
  alcohol_lore_lore: +8
abilityMods: [-1,1,2,4,0,3]

ac: 16 # unrendered
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +8; __Ref__: +7; __Will__: +4"
hp: 28 # unrendered
health:
  - name: "HP"
    desc: 28
saves: # unrendered
  fortitude: +8
  reflex: +7
  will: +4

speed: 25 feet
attacks:
  - name: "Melee"
    desc: "⬻ dagger +5 (Agile, Finesse, Thrown 10, Versatile S) __Damage__ 1d4-1 piercing"
  - name: "Ranged"
    desc: "⬻ versatile vial +1 (Acid, Alchemical, Bomb, Consumable, Infused, Splash) __Range__ 20 ft.; __Reload__ -; __Damage__ 1d6 acid"
  - name: "Ranged"
    desc: "⬻ nail bomb (lesser) +1 (Alchemical, Bomb, Consumable, Splash) __Range__ 20 ft.; __Reload__ -; __Damage__ 2d4 piercing"
  - name: "Ranged"
    desc: "⬻ steelscour (lesser) +1 (Acid, Alchemical, Bomb, Consumable) __Range__ 20 ft.; __Reload__ -; __Damage__ 0 acid"
```

## Feats and Features

### Class Features

**Advanced Alchemy** *Level 1*

`alchemist`

During your daily preparations, you spend some time to create alchemical items that can be used over the course of the day.

You don't need to attempt a Crafting check to do this, you can use an alchemist's toolkit instead of an alchemist's lab, and you ignore both the number of days typically required to create the items and any alchemical raw materials requirements.

You can Craft a number of alchemical items up to 4 + your Intelligence modifier. Each item must be in your formula book, have an item level equal to or lower than your level, and have the consumable trait.

These items have the infused trait and remain potent for 24 hours or until your next daily preparations, whichever comes first.

**Alchemy** *Level 1*

`alchemist`

You understand the reactions between all manner of reagents and can concoct alchemical items to meet your needs. You can do this using normal reagents and the Craft activity, or you can use specially prepared chemicals that allow you to craft temporary items quickly and at no cost. Over time, you can create more and more alchemical items for free, and since each of them becomes more and more powerful, you advance in power dramatically, leaving behind those who don't understand your strange science.

You gain the Alchemical Crafting feat, and you can automatically identify alchemical items that you have the formula for.

**Chirurgeon** *Level 1*

`alchemist`

You concentrate on healing others with alchemy.

**Formulas** Two common 1st-level alchemical elixirs with the healing trait (like lesser antidote, lesser antiplague, or minor elixir of life).

**Field Benefit** You can use your proficiency rank in Crafting for anything that requires a proficiency rank in Medicine (such as prerequisites) and use your Crafting modifier in place of your Medicine modifier for all Medicine checks.

**Field Vials** Your versatile vials can be used to heal a living creature a number of Hit Points equal to the vial's initial damage. A creature can drink the vial for this benefit, or you can throw the vial at a willing creature within 20 feet as an Interact action to heal that creature. In either case, a vial used this way loses the acid and splash traits and gains the coagulant and healing traits, plus the elixir trait if a creature drinks it.

**Field Discovery (5th)** Your medicinal elixirs are quite fortifying. When a creature drinks an infused elixir with the healing trait that you have created, that creature gains a number of temporary Hit Points equal to your Intelligence modifier (minimum 0); these temporary Hit Points last for 1 minute.

**Advanced Vials (11th)** When you use a field vial to heal a creature that has half its maximum Hit Points or fewer, the coagulant trait doesn't apply to that healing.

**Greater Field Discovery (13th)** When you use Quick Alchemy to create any type of elixir of life, the creature healed by the item regains the maximum Hit Points possible, instead of rolling to determine the number of Hit Points regained.

**Formula Book** *Level 1*

`alchemist`

An alchemist keeps meticulous formulas for every item they can create. You start with a standard Formula Book for free. The formula book contains the formulas for two common 1st-level alchemical items of your choice, in addition to any formulas you gained from Alchemical Crafting and your research field.

Each time you gain a level, you can add the formulas for two common alchemical items to your formula book. These new formulas can be for any level of item you can create. You learn these formulas automatically, but it's also possible to find or buy additional formulas in settlements or from other alchemists, or to select the Inventor skill feat so you can invent them.

As normal, having the base formula is sufficient when Crafting upgraded types of the item—you don't need to learn higher-level formulas. For instance, if you have the 1st-level formula for a minor elixir of life, you can create a minor, lesser, moderate, greater, major, or true elixir of life as long as you meet the level and other prerequisites. Items with type entries that have widely varied functions require separate formulas, but most alchemical items have a structure similar to elixir of life.

**Quick Alchemy** *Level 1*

`alchemist`

You gain the Quick Alchemy action to make the items you need on the fly.

**Research Field** *Level 1*

`alchemist`

Your inquiries into the alchemical nature of the universe have led you to focus on a particular field of research. At 1st level, you choose your research field. This choice gives you more formulas, a special benefit, other abilities for your versatile vials, and other benefits as you level up.

**Versatile Vials** *Level 1*

`alchemist`

You know how to prepare fast-acting chemicals into versatile vials, special items that can be used as bombs and be turned into other alchemical items by introducing special reagents. During your daily preparations, you can create a number of versatile vials up to 2 + your Intelligence modifier, which is also your maximum number of vials. If you're below your maximum number, you can gather reagents from the environment around you. For every 10 minutes you spend in exploration mode, you regain 2 vials; this doesn't prevent you from participating in other exploration activities.

Versatile vials are infused items, and are destroyed if not used by the next time you make your daily preparations. A vial you create is always the highest type you could Craft. See the sidebar for statistics on using a versatile vial as a bomb. You can also use vials for Quick Alchemy and your research field can add to the ways you can use a vial.

You can store all your versatile vials within your Alchemist's Toolkit, with no increase to its Bulk. Though versatile vials are physical objects, they can't be duplicated or preserved in any way.

### Class Feats

**Quick Bomber** *Level 1*

`alchemist`

You keep your bombs and bomb-related reagents in easy-toreach pouches from which you draw without thinking. You Interact to draw a bomb, draw a versatile vial, or use Quick Alchemy to create a bomb, then Strike with the bomb. If you have the ability to create more than one bomb at a time with Quick Alchemy (such as from the double brew class feature), you can Strike with only one of the bombs you create with this action.

**Smoke Bomb** *Level 2*

`additive`  `alchemist`

You can add a tarry additive to an alchemical bomb to make it emit smoke. When thrown, in addition to its normal effects, the bomb creates a cloud of smoke in a area. You choose which corner of the target's space (or the space in which the bomb lands) the cloud is centered on. Creatures within that area have the Concealed condition, and all other creatures are concealed to them. The smoke lasts for 1 minute or until dissipated by a strong wind.

### Ancestry Feats

**Animal Accomplice** *Level 1*

`gnome`

You build a rapport with an animal, which becomes magically bonded to you. You gain a familiar. The type of animal is up to you, but most gnomes choose animals with a burrow Speed.

### Skill Feats

**Alchemical Crafting** *Level 1*

`general`  `skill`

You can use the Craft activity to create alchemical items. When you select this feat, you immediately add the formulas for four common 1st-level alchemical items to your formula book.

**Alchemical Crafting** *Level 1*

`general`  `skill`

You can use the Craft activity to create alchemical items. When you select this feat, you immediately add the formulas for four common 1st-level alchemical items to your formula book.

**Alchemical Crafting** *Level 1*

`general`  `skill`

You can use the Craft activity to create alchemical items. When you select this feat, you immediately add the formulas for four common 1st-level alchemical items to your formula book.

**Hobnobber** *Level 1*

`general`  `skill`

You are skilled at learning information through conversation. The Gather Information exploration activity takes you half as long as normal (typically reducing the time to 1 hour). If you're a master in Diplomacy and roll a critical failure to Gather Information, you get a failure instead. There is still no guarantee that a rumor you learn with Gather Information is accurate.

**Read Lips** *Level 1*

`general`  `skill`

You can read lips of others nearby who you can clearly see. The language read must be one that you know. When you're at your leisure, you can do this automatically. In encounter mode or when attempting a more difficult feat of lipreading, you're Fascinated and Off-Guard during each round in which you focus on lip movements, and you must succeed at a Society check (DC determined by the GM) to successfully read someone's lips.

**Seasoned** *Level 1*

`general`  `skill`

You've mastered the preparation of many types of food and drink. You gain a +1 circumstance bonus to checks to Craft food and drink, including elixirs if you have Alchemical Crafting and potions if you have Magical Crafting. If you are a master in one of the prerequisite skills, this bonus increases to +2.

### General Feats

**Pet** *Level 1*

`general`

You have a pet—a Tiny animal of a type you choose, such as a cat, bird, or rodent. It has the minion trait, meaning it gains 2 actions during your turn if you use the Command an Animal action to command it; this replaces the usual effects of Command an Animal, and you don't need to attempt a Nature check. A pet can't make Strikes.

**Level** Your pet's level is equal to yours.

**Modifiers and AC** Your pet's save modifiers and AC are equal to yours before applying circumstance or status bonuses or penalties. It uses 3 + your level as its modifier for Perception, Acrobatics, and Stealth, and just your level as its modifier for other skill checks. It doesn't have or use its own attribute modifiers and can never benefit from item bonuses.

**Hit Points** Your pet has 5 Hit Points per level.

**Senses** Your pet has low-light vision and can gain additional senses from pet abilities.

**Speed** Your pet has a Speed of 25 feet. You can choose to instead have an aquatic pet, which breathes in water instead of air and has the aquatic trait, no land Speed, and a swim Speed of 25 feet.

**Pet Abilities** When you gain your pet, choose two of the following abilities. If your pet is an animal that naturally has one of these abilities (for instance, an owl has a fly Speed), you must select that ability. Your pet can't be an animal that naturally has more pet abilities than the maximum. In some cases, the GM might add some familiar abilities to the pet abilities you can choose.

- **Amphibious** It gains the amphibious trait, allowing it to breathe in both air and water, and has both a land Speed and a swim Speed, each equal to its highest land Speed or swim Speed.

- **Burrower** It gains a burrow Speed of 5 feet, allowing it to dig Tiny holes.

- **Climber** It gains a climb Speed of 25 feet.

- **Darkvision** It gains darkvision.

- **Echolocation** Your pet can use hearing as a precise sense within 20 feet.

- **Fast** Movement Increase one of the pet's Speeds from 25 feet to 40 feet.

- **Flier** It gains a fly Speed of 25 feet.

- **Manual Dexterity** It can use up to two of its limbs as if they were hands to perform manipulate actions.

- **Scent** Your pet can use scent as an imprecise sense within 30 feet

- **Tough** Your pet's max HP increase by 2 per level.

**Special** You can gain a new pet by retraining this feat, releasing any previous pet you have. If you later gain a familiar or other companion that uses the Pet feat, you can immediately retrain this feat.


## Inventory

### Currency

| Denomination | Qty |
|---|---|
| Silver (sp) | 5 |
| Copper (cp) | 1 |
| **Total** | **0.51 gp** |

### Held

| Item | Qty | Bulk | Price |
|---|---|---|---|
| Buckler |  | 0.1 | 1 gp |
| Dagger |  | 0.1 | 2 sp |
| Versatile Vial | 4 |  |  |

### Worn and Invested

| Item | Qty | Bulk | Price |
|---|---|---|---|
| Backpack |  |  | 1 sp |
| Leather Armor |  | 1 | 2 gp |

### Carried

| Item | Qty | Bulk | Price |
|---|---|---|---|
| Alchemist's Toolkit |  | 1 | 3 gp |
| Alcohol | 5 | 0.1 | 1 cp |
| Bedroll |  | 0.1 | 2 cp |
| Bravo's Brew (Lesser) |  | 0.1 | 7 gp |
| Formula Book (Blank) |  | 0.1 | 1 gp |
| Harrow Deck (Simple) |  | 0.1 | 1 gp |
| Infiltrator's Elixir |  | 0.1 | 6 gp |
| Nail Bomb (Lesser) |  | 0.1 | 8 gp |
| Rope |  | 0.1 | 5 sp |
| Steelscour (Lesser) |  | 0.1 | 3 gp |

## Companion: Sir Pickles

*Rat familiar. Uses Gripp's AC, saving throws and Perception,
and has 5 Hit Points per level. These values are derived from
Gripp's sheet; a familiar stores none of its own.*

```statblock
layout: Basic Pathfinder 2e Layout
name: Sir Pickles
level: 2

rare_03: Familiar # class
rare_04: Gripp's companion # background
size: Tiny
trait_01: Rat
trait_02: Minion

modifier: 4 # unrendered
perception:
  - name: Perception
    desc: "Perception +4"
abilityMods: [0,0,0,0,0,0]

ac: 16 # unrendered
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +8; __Ref__: +7; __Will__: +4"
hp: 10 # unrendered
health:
  - name: "HP"
    desc: 10

speed: 25 feet
```

### Sir Pickles's Abilities

- **Item Delivery**
- **Manual Dexterity**
