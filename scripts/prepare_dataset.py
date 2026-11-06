import os
import random
import shutil

# ============================================================
# CONFIGURATION
# ============================================================

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOURCE_ROOT = os.path.join(
    PROJECT_ROOT,
    "data",
    "dataset",
    "plantvillage_temp",
    "raw",
    "color"
)

OUTPUT_ROOT = os.path.join(
    PROJECT_ROOT,
    "data",
    "processed"
)

IMAGES_PER_CLASS = 500

RANDOM_SEED = 42

random.seed(RANDOM_SEED)


# ============================================================
# CLASS MAPPING
# ============================================================

CLASS_MAPPING = {
    "Tomato___healthy": "healthy",
    "Tomato___Early_blight": "early_blight",
    "Tomato___Late_blight": "late_blight",
    "Tomato___Leaf_Mold": "leaf_mold"
}


# ============================================================
# CREATE OUTPUT DIRECTORIES
# ============================================================

splits = ["train", "validation", "test"]

for split in splits:
    for class_name in CLASS_MAPPING.values():
        folder = os.path.join(
            OUTPUT_ROOT,
            split,
            class_name
        )

        os.makedirs(folder, exist_ok=True)


# ============================================================
# PROCESS EACH CLASS
# ============================================================

for source_class, output_class in CLASS_MAPPING.items():

    source_folder = os.path.join(
        SOURCE_ROOT,
        source_class
    )

    print("\nProcessing:", source_class)

    if not os.path.exists(source_folder):
        print("ERROR: Source folder not found:")
        print(source_folder)
        continue

    # Get image files
    image_files = [
        file for file in os.listdir(source_folder)
        if file.lower().endswith(
            (".jpg", ".jpeg", ".png")
        )
    ]

    print("Available images:", len(image_files))

    # Shuffle deterministically
    random.shuffle(image_files)

    # Make sure enough images exist
    if len(image_files) < IMAGES_PER_CLASS:
        print(
            f"WARNING: Only {len(image_files)} images available. "
            f"Using all available images."
        )

        selected_images = image_files

    else:
        selected_images = image_files[:IMAGES_PER_CLASS]

    # Calculate split sizes
    total = len(selected_images)

    train_end = int(total * 0.80)
    validation_end = int(total * 0.90)

    train_images = selected_images[:train_end]

    validation_images = selected_images[
        train_end:validation_end
    ]

    test_images = selected_images[
        validation_end:
    ]

    split_data = {
        "train": train_images,
        "validation": validation_images,
        "test": test_images
    }

    # Copy files
    for split, files in split_data.items():

        destination_folder = os.path.join(
            OUTPUT_ROOT,
            split,
            output_class
        )

        for file in files:

            source_path = os.path.join(
                source_folder,
                file
            )

            destination_path = os.path.join(
                destination_folder,
                file
            )

            shutil.copy2(
                source_path,
                destination_path
            )

        print(
            f"{split}: {len(files)} images"
        )


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("DATASET PREPARATION COMPLETE")
print("=" * 60)

for split in splits:

    print(f"\n{split.upper()}")

    for class_name in CLASS_MAPPING.values():

        folder = os.path.join(
            OUTPUT_ROOT,
            split,
            class_name
        )

        count = len([
            file for file in os.listdir(folder)
            if file.lower().endswith(
                (".jpg", ".jpeg", ".png")
            )
        ])

        print(
            f"{class_name:15s}: {count}"
        )