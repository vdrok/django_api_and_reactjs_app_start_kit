import React, {Component} from 'react';
import { withStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';
import ProfileStatusButton from './ProfileStatusButton';
import { adminStyles } from 'styles';


class ProfileStatusButtons extends Component {

  render() {
    const { profile, classes } = this.props;

    return(
    <Grid container spacing={24}>
        <Grid item xs={4} >
          <ProfileStatusButton link="/admin/head-line" requireApproval={true} title="Headline, Bio & Resume" />
        </Grid>
        <Grid item xs={4} >
          <ProfileStatusButton link="#" requireApproval={true} title="Pictures" />
        </Grid>
        <Grid item xs={4} >
          <ProfileStatusButton link="#" requireApproval={true} title="Videos" />
        </Grid>
        <Grid item xs={4} >
          <ProfileStatusButton link="#" requireApproval={false} title="Casting Requests" />
        </Grid>
        <Grid item xs={4} >
          <ProfileStatusButton link="#" requireApproval={false} title="Profile Notes" />
        </Grid>
        <Grid item xs={4} >
          <ProfileStatusButton link="#" requireApproval={false} title="Logs & Lockouts" />
        </Grid>
        <Grid item xs={4} >
          <ProfileStatusButton link="#" requireApproval={false} title="Searches / Views" />
        </Grid>
        <Grid item xs={4} >
          <ProfileStatusButton link="#" requireApproval={false} title="Shares" />
        </Grid>
        <Grid item xs={4} >
          <ProfileStatusButton link="#" requireApproval={false} title="Blocks" />
        </Grid>
        <Grid item xs={4} >
          <ProfileStatusButton link="#" requireApproval={false} title="Ratings" />
        </Grid>
        <Grid item xs={4} >
          <ProfileStatusButton link="#" requireApproval={false} title="Contracts" />
        </Grid>
        <Grid item xs={4} >
          <ProfileStatusButton link="#" requireApproval={true} title="Medical" />
        </Grid>
        <Grid item xs={4} >
          <ProfileStatusButton link="#" requireApproval={false} title="Credentials" />
        </Grid>
        <Grid item xs={4} >
          <ProfileStatusButton link="#" requireApproval={true} title="Personal Info" />
        </Grid>
        <Grid item xs={4} >
          <ProfileStatusButton link="#" requireApproval={true} title="Immigration" />
        </Grid>
        <Grid item xs={4} >
          <ProfileStatusButton link="#" requireApproval={true} title="Languages" />
        </Grid>
        <Grid item xs={4} >
          <ProfileStatusButton link="#" requireApproval={false} title="Finance" />
        </Grid>
        <Grid item xs={4} >
          <ProfileStatusButton link="#" requireApproval={false} title="Calendar" />
        </Grid>
    </Grid>  

    );
  }

}

export default withStyles(adminStyles)(ProfileStatusButtons);