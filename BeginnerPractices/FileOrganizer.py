#Detail of project-
#Features: Move images, videos, and documents into separate folders
# Concepts: os, pathlib, File Handling
# Challenge: Handle duplicate file names.



# ============================================================
#  🗂️  ROGUE'S FILE ORGANIZER
#  "Your folder is a crime scene. This is the detective."
# ============================================================

import os
from pathlib import Path
from datetime import datetime

# ── THE CATEGORY MAP ─────────────────────────────────────────
# Extension → which folder it belongs in
CATEGORIES = {
    # 🖼️ Images
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images",
    ".gif": "Images", ".webp": "Images", ".svg": "Images",
    ".bmp": "Images", ".ico": "Images", ".tiff": "Images",

    # 🎬 Videos
    ".mp4": "Videos", ".mov": "Videos", ".avi": "Videos",
    ".mkv": "Videos", ".wmv": "Videos", ".flv": "Videos",
    ".webm": "Videos", ".m4v": "Videos",

    # 🎵 Audio
    ".mp3": "Audio", ".wav": "Audio", ".flac": "Audio",
    ".aac": "Audio", ".ogg": "Audio", ".m4a": "Audio",

    # 📄 Documents
    ".pdf": "Documents", ".docx": "Documents", ".doc": "Documents",
    ".txt": "Documents", ".xlsx": "Documents", ".xls": "Documents",
    ".pptx": "Documents", ".ppt": "Documents", ".csv": "Documents",

    # 💻 Code
    ".py": "Code", ".js": "Code", ".html": "Code",
    ".css": "Code", ".json": "Code", ".xml": "Code",
    ".cpp": "Code", ".java": "Code", ".ts": "Code",

    # 📦 Archives
    ".zip": "Archives", ".rar": "Archives", ".7z": "Archives",
    ".tar": "Archives", ".gz": "Archives",
}

# ── STATS TRACKER ────────────────────────────────────────────
stats = {
    "moved": 0,
    "duplicates_renamed": 0,
    "skipped": 0,
    "categories_used": set()
}


# ── THE DUPLICATE SLAYER ──────────────────────────────────────
def resolve_duplicate(destination: Path) -> Path:
    """
    If destination already exists, keeps adding _1, _2, _3...
    until it finds a name that's free. Nobody gets overwritten.
    """
    if not destination.exists():
        return destination  # no conflict, go straight in

    stem = destination.stem       # "naruto"    from "naruto.jpg"
    suffix = destination.suffix   # ".jpg"      from "naruto.jpg"
    parent = destination.parent   # "Images/"   folder path
    counter = 1

    while True:
        new_name = f"{stem}_{counter}{suffix}"   # "naruto_1.jpg"
        new_destination = parent / new_name
        if not new_destination.exists():
            return new_destination               # free slot found ✅
        counter += 1


# ── THE REPORT PRINTER ───────────────────────────────────────
def print_report(log: list):
    """Prints a cinematic summary after the job is done."""
    line = "─" * 52

    print(f"\n{line}")
    print("   📋  MISSION REPORT")
    print(f"{line}")

    if not log:
        print("   Nothing was moved. Folder was already clean.")
    else:
        for entry in log:
            print(entry)

    print(f"{line}")
    print(f"   ✅  Moved          : {stats['moved']} files")
    print(f"   🔁  Renamed (dupe) : {stats['duplicates_renamed']} files")
    print(f"   ⏭️   Skipped        : {stats['skipped']} files")
    print(f"   📁  Folders used   : {', '.join(sorted(stats['categories_used'])) or 'None'}")
    print(f"{line}\n")


# ── THE CORE ORGANIZER ───────────────────────────────────────
def organize(folder_path: str):
    """
    The brain. Scans every file, decides where it belongs,
    handles duplicates, moves it, logs everything.
    """
    folder = Path(folder_path)

    # ── Guard: does this folder even exist?
    if not folder.exists():
        print(f"\n🚫 Folder not found: '{folder_path}'")
        print("   Double-check the path and try again.\n")
        return

    if not folder.is_dir():
        print(f"\n🚫 '{folder_path}' is a file, not a folder.\n")
        return

    print(f"\n{'═' * 52}")
    print(f"   🗂️   ROGUE'S FILE ORGANIZER — ACTIVATED")
    print(f"   📍  Target : {folder}")
    print(f"   🕐  Time   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'═' * 52}")
    print("   Scanning...\n")

    log = []

    for file in folder.iterdir():

        # ── Skip folders — only touch files
        if file.is_dir():
            stats["skipped"] += 1
            continue

        # ── Read the extension (lowercased so .JPG == .jpg)
        extension = file.suffix.lower()

        # ── Decide the category
        category = CATEGORIES.get(extension, "Misc")

        # ── Build the destination folder path and create it
        dest_folder = folder / category
        dest_folder.mkdir(exist_ok=True)   # creates folder, won't crash if exists

        # ── Build the full destination file path
        destination = dest_folder / file.name

        # ── Handle duplicate — rename until slot is free
        final_destination = resolve_duplicate(destination)

        was_renamed = final_destination.name != file.name

        # ── The actual move
        file.rename(final_destination)

        # ── Update stats
        stats["moved"] += 1
        stats["categories_used"].add(category)

        if was_renamed:
            stats["duplicates_renamed"] += 1
            tag = f"🔁 RENAMED"
            log.append(
                f"   {tag:<12} {file.name}  →  {category}/{final_destination.name}"
            )
        else:
            log.append(
                f"   ✅ MOVED       {file.name}  →  {category}/"
            )

    # ── Print the full mission report
    print_report(log)


# ── THE UNDO SYSTEM (BONUS) ──────────────────────────────────
def undo_organize(folder_path: str):
    """
    Pulls everything back out of subfolders into the root folder.
    Your 'ctrl+z' if you regret the clean-up.
    """
    folder = Path(folder_path)
    known_folders = set(CATEGORIES.values()) | {"Misc"}
    moved_back = 0

    print(f"\n{'═' * 52}")
    print(f"   ↩️   UNDO MODE — Reversing the organization")
    print(f"{'═' * 52}\n")

    for subfolder in folder.iterdir():
        if subfolder.is_dir() and subfolder.name in known_folders:
            for file in subfolder.iterdir():
                if file.is_file():
                    destination = folder / file.name
                    final = resolve_duplicate(destination)
                    file.rename(final)
                    moved_back += 1
                    print(f"   ↩️  {subfolder.name}/{file.name}  →  root")
            subfolder.rmdir()   # remove now-empty subfolder

    print(f"\n   Done. {moved_back} files returned to root folder.\n")


# ── MAIN MENU ────────────────────────────────────────────────
def main():
    print("\n" + "═" * 52)
    print("      🗂️  ROGUE'S FILE ORGANIZER v1.0")
    print("   'Your chaos is temporary. This script is forever.'")
    print("═" * 52)

    while True:
        print("\n  What do you want to do?")
        print("  1. Organize a folder")
        print("  2. Undo organization (put files back)")
        print("  3. Exit")
        print("─" * 35)

        choice = input("  Enter choice (1/2/3): ").strip()

        if choice == "1":
            path = input("\n  📂 Paste the folder path: ").strip().strip('"')
            organize(path)

        elif choice == "2":
            path = input("\n  📂 Paste the folder path to undo: ").strip().strip('"')
            undo_organize(path)

        elif choice == "3":
            print("\n  👋 Stay organized, Rogue. Peace.\n")
            break

        else:
            print("  ⚠️  Type 1, 2, or 3. Nothing else.")


# ── ENTRY POINT ──────────────────────────────────────────────
if __name__ == "__main__":
    main()