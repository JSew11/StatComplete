import './index.css';

export default function Error({ errorRef, message }) {
  return (
    <div ref={errorRef} className={message ? 'error-msg' : 'offscreen'}
      aria-live='assertive'>
        {message}
    </div>
  );
}