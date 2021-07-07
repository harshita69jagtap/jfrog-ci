This Repo is for syncing the webhook with the pipeline type of Github Integration

This integration is used for adding the pipeline source and for creating GitRepo typr of Resource

Any commit to the master branch of this repo triggers an update to the webhook updating it's payload section which in turn update the GitRepo Resource hence triggering execution of first step of pipeline workflow.
