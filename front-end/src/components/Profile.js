import React from 'react';

const Profile = ({ data }) => {
  return (
    <div>
      <h2>Profile Component</h2>
      <p>Full Name :{data.fullName}</p>
      <p>Email :{data.email}</p>
    </div>
  );
};

export default Profile;