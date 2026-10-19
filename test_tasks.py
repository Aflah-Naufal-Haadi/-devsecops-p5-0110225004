
import unittest
from unittest.mock import patch

from tasks import add_task, finish_task
from summary import task_summary


class TestPengelolaanTugas(unittest.TestCase):

    def test_tambah_tugas(self):
        with patch("tasks.load_tasks", return_value=[]), \
             patch("tasks.save_tasks") as simpan:
            tugas = add_task("Mengerjakan tugas kuliah")

            self.assertEqual(tugas["id"], 1)
            self.assertEqual(
                tugas["title"],
                "Mengerjakan tugas kuliah"
            )
            self.assertFalse(tugas["completed"])
            simpan.assert_called_once()

    def test_judul_kosong_ditolak(self):
        with self.assertRaises(ValueError):
            add_task("   ")

    def test_menandai_tugas_selesai(self):
        daftar_tugas = [
            {
                "id": 1,
                "title": "Belajar Python",
                "completed": False
            }
        ]

        with patch(
            "tasks.load_tasks",
            return_value=daftar_tugas
        ), patch("tasks.save_tasks"):
            tugas = finish_task("1")
            self.assertTrue(tugas["completed"])

    def test_ringkasan_tugas(self):
        daftar_tugas = [
            {"id": 1, "title": "Tugas A", "completed": True},
            {"id": 2, "title": "Tugas B", "completed": False}
        ]

        hasil = task_summary(daftar_tugas)

        self.assertEqual(hasil["total"], 2)
        self.assertEqual(hasil["completed"], 1)
        self.assertEqual(hasil["pending"], 1)


if __name__ == "__main__":
    unittest.main()
