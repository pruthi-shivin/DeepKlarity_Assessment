function Modal({
  children,
  onClose
}) {

  return (

    <div className="modal-overlay">

      <div className="modal">

        {children}

        <button
          className="close-btn"
          onClick={onClose}
        >
          Close
        </button>

      </div>

    </div>
  );
}

export default Modal;