from tasks import add_task, get_tasks, finish_task
from summary import task_summary


def main():
    while True:
        print("\n=== PENGELOLAAN TUGAS ===")
        print("1. Tambah tugas")
        print("2. Lihat tugas")
        print("3. Tandai tugas selesai")
        print("4. Ringkasan tugas")
        print("0. Keluar")

        choice = input("Pilih menu: ").strip()

        try:
            if choice == "1":
                title = input("Masukkan judul tugas: ")
                task = add_task(title)
                print(f"Tugas berhasil ditambahkan. ID: {task['id']}")

            elif choice == "2":
                tasks = get_tasks()

                if not tasks:
                    print("Belum ada tugas.")
                else:
                    for task in tasks:
                        status = (
                            "Selesai"
                            if task["completed"]
                            else "Belum selesai"
                        )
                        print(f"{task['id']}. {task['title']} - {status}")

            elif choice == "3":
                task_id = input("Masukkan ID tugas: ")
                task = finish_task(task_id)
                print(f"Tugas '{task['title']}' sudah selesai.")

            elif choice == "4":
                result = task_summary(get_tasks())
                print(f"Total tugas    : {result['total']}")
                print(f"Tugas selesai  : {result['completed']}")
                print(f"Belum selesai  : {result['pending']}")

            elif choice == "0":
                print("Terima Kasih.")
                break

            else:
                print("Pilihan tidak tersedia.")

        except ValueError as error:
            print(f"Kesalahan: {error}")
        except OSError:
            print("Terjadi masalah saat mengakses file data.")


if __name__ == "__main__":
    main()