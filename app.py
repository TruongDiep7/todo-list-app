
# Danh sách để lưu các công việc
tasks = []


def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append({
        "name": task_name,
        "completed": False
    })
    print(f"Đã thêm công việc: '{task_name}'")


def complete_task(task_index):
    """Đánh dấu công việc đã hoàn thành."""
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        print(f"Đã hoàn thành: '{tasks[task_index - 1]['name']}'")
    else:
        print("Số thứ tự công việc không hợp lệ.")


def list_tasks():
    """Hiển thị danh sách công việc."""
    if not tasks:
        print("Danh sách công việc đang trống.")
    else:
        print("Danh sách công việc:")
        for index, task in enumerate(tasks, start=1):
            status = "[x]" if task["completed"] else "[ ]"
            print(f"{index}. {status} {task['name']}")


# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")

    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")

    list_tasks()

    print("\nĐánh dấu công việc số 1 đã hoàn thành:")
    complete_task(1)

    print("\nDanh sách sau khi cập nhật:")
    list_tasks()
