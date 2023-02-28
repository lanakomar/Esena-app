import { useSelector } from "react-redux";
import { useState, useEffect } from "react";

import { Modal } from "../../context/Modal";
import TaskModal from "../TaskModal/TaskModal";
import SideBar from "../SideBar";
import "./index.css";

import Kalend, { CalendarView } from "kalend"; // import component
import "kalend/dist/styles/index.css"; // import styles

const MyCalendar = () => {
  const sessionUser = useSelector((state) => state.session.user);
  const tasksObj = useSelector((state) => state.tasks);

  const [events, setEvents] = useState([]);
  const [selectedView, setSelectedView] = useState("month");
  const [showModal, setShowModal] = useState(false);
  const [clickedTaskId, setClickedTaskId] = useState();

  useEffect(() => {
    const colors = {
      1: "rgba(186, 207, 249, 0.4)",
      2: "rgba(239, 221, 211, 0.4)",
      3: "rgba(245, 189, 191, 0.4)",
    };
    let allTasks = Object.values(tasksObj);
    allTasks = allTasks?.filter((task) => task.assignee_id == sessionUser?.id);
    const eventsArr = allTasks?.map((task) => {
      const start = new Date(task.create_date);
      start.setHours(8);
      const end = new Date(task.end_date);
      end.setHours(19);
      return {
        id: task.id,
        startAt: start.toISOString(),
        endAt: end.toISOString(),
        summary: task.name,
        color: colors[task.priority_id],
        timezoneStartAt: "America/Los_Angeles",
      };
    });
    setEvents(eventsArr);
  }, [tasksObj, sessionUser]);

  const onSelectView = (view) => {
    setSelectedView(view);
  };

  const handleEventClick = (task) => {
    console.log("??????????", task);
    setClickedTaskId(task.id);
    setShowModal(true);
  };

  return (
    <div className="calendar-page-container">
      <SideBar />
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <TaskModal taskId={clickedTaskId} />
        </Modal>
      )}
      <div className="calendar-legend">
        <div className="color-box-container">
          <div className="color-box-low"></div>
          <div className="color-box-label">Low Priority</div>
        </div>
        <div className="color-box-container">
          <div className="color-box-medium"></div>
          <div className="color-box-label">Medium Priority</div>
        </div>
        <div className="color-box-container">
          <div className="color-box-high"></div>
          <div className="color-box-label">High Priority</div>
        </div>
      </div>
      <div
        className={
          selectedView === "month"
            ? "calendar-container month-view"
            : "calendar-container"
        }
      >
        <Kalend
          events={events}
          initialView={CalendarView.AGENDA}
          initialDate={new Date().toISOString()}
          disabledViews={[CalendarView.THREE_DAYS]}
          onSelectView={onSelectView}
          onEventClick={(task) => handleEventClick(task)}
        />
      </div>
    </div>
  );
};

export default MyCalendar;
